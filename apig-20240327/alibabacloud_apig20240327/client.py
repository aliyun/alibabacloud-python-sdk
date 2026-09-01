# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_apig20240327 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
            'ap-southeast-2': 'apig.ap-southeast-2.aliyuncs.com',
            'ap-southeast-6': 'apig.ap-southeast-6.aliyuncs.com',
            'ap-southeast-7': 'apig.ap-southeast-7.aliyuncs.com',
            'cn-guangzhou': 'apig.cn-guangzhou.aliyuncs.com',
            'cn-heyuan': 'apig.cn-heyuan.aliyuncs.com',
            'cn-shenzhen': 'apig.cn-shenzhen.aliyuncs.com',
            'cn-wulanchabu': 'apig.cn-wulanchabu.aliyuncs.com',
            'cn-beijing': 'apig.cn-beijing.aliyuncs.com',
            'ap-northeast-2': 'apig.ap-northeast-2.aliyuncs.com',
            'ap-northeast-1': 'apig.ap-northeast-1.aliyuncs.com',
            'cn-chengdu': 'apig.cn-chengdu.aliyuncs.com',
            'cn-qingdao': 'apig.cn-qingdao.aliyuncs.com',
            'cn-shanghai': 'apig.cn-shanghai.aliyuncs.com',
            'cn-hongkong': 'apig.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'apig.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'apig.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'apig.ap-southeast-5.aliyuncs.com',
            'cn-zhangjiakou': 'apig.cn-zhangjiakou.aliyuncs.com',
            'cn-hangzhou': 'apig.cn-hangzhou.aliyuncs.com',
            'us-west-1': 'apig.us-west-1.aliyuncs.com',
            'us-east-1': 'apig.us-east-1.aliyuncs.com',
            'eu-central-1': 'apig.eu-central-1.aliyuncs.com',
            'eu-west-1': 'apig.eu-west-1.aliyuncs.com',
            'me-east-1': 'apig.me-east-1.aliyuncs.com',
            'me-central-1': 'apig.me-central-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('apig', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_gateway_quota_rule_with_options(
        self,
        gateway_id: str,
        request: main_models.AddGatewayQuotaRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayQuotaRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conflict_hash):
            body['conflictHash'] = request.conflict_hash
        if not DaraCore.is_null(request.consumer_group_ids):
            body['consumerGroupIds'] = request.consumer_group_ids
        if not DaraCore.is_null(request.consumer_ids):
            body['consumerIds'] = request.consumer_ids
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.overwrite):
            body['overwrite'] = request.overwrite
        if not DaraCore.is_null(request.period_multiplier):
            body['periodMultiplier'] = request.period_multiplier
        if not DaraCore.is_null(request.period_type):
            body['periodType'] = request.period_type
        if not DaraCore.is_null(request.quota_dimension):
            body['quotaDimension'] = request.quota_dimension
        if not DaraCore.is_null(request.quota_limit):
            body['quotaLimit'] = request.quota_limit
        if not DaraCore.is_null(request.rule_name):
            body['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.subject_type):
            body['subjectType'] = request.subject_type
        if not DaraCore.is_null(request.timezone):
            body['timezone'] = request.timezone
        if not DaraCore.is_null(request.window_alignment):
            body['windowAlignment'] = request.window_alignment
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayQuotaRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayQuotaRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_quota_rule_with_options_async(
        self,
        gateway_id: str,
        request: main_models.AddGatewayQuotaRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewayQuotaRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conflict_hash):
            body['conflictHash'] = request.conflict_hash
        if not DaraCore.is_null(request.consumer_group_ids):
            body['consumerGroupIds'] = request.consumer_group_ids
        if not DaraCore.is_null(request.consumer_ids):
            body['consumerIds'] = request.consumer_ids
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.overwrite):
            body['overwrite'] = request.overwrite
        if not DaraCore.is_null(request.period_multiplier):
            body['periodMultiplier'] = request.period_multiplier
        if not DaraCore.is_null(request.period_type):
            body['periodType'] = request.period_type
        if not DaraCore.is_null(request.quota_dimension):
            body['quotaDimension'] = request.quota_dimension
        if not DaraCore.is_null(request.quota_limit):
            body['quotaLimit'] = request.quota_limit
        if not DaraCore.is_null(request.rule_name):
            body['ruleName'] = request.rule_name
        if not DaraCore.is_null(request.subject_type):
            body['subjectType'] = request.subject_type
        if not DaraCore.is_null(request.timezone):
            body['timezone'] = request.timezone
        if not DaraCore.is_null(request.window_alignment):
            body['windowAlignment'] = request.window_alignment
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewayQuotaRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewayQuotaRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_quota_rule(
        self,
        gateway_id: str,
        request: main_models.AddGatewayQuotaRuleRequest,
    ) -> main_models.AddGatewayQuotaRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_gateway_quota_rule_with_options(gateway_id, request, headers, runtime)

    async def add_gateway_quota_rule_async(
        self,
        gateway_id: str,
        request: main_models.AddGatewayQuotaRuleRequest,
    ) -> main_models.AddGatewayQuotaRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_gateway_quota_rule_with_options_async(gateway_id, request, headers, runtime)

    def add_gateway_security_group_rule_with_options(
        self,
        gateway_id: str,
        request: main_models.AddGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewaySecurityGroupRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.port_ranges):
            body['portRanges'] = request.port_ranges
        if not DaraCore.is_null(request.security_group_id):
            body['securityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewaySecurityGroupRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/security-group-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewaySecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_gateway_security_group_rule_with_options_async(
        self,
        gateway_id: str,
        request: main_models.AddGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddGatewaySecurityGroupRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.port_ranges):
            body['portRanges'] = request.port_ranges
        if not DaraCore.is_null(request.security_group_id):
            body['securityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddGatewaySecurityGroupRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/security-group-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGatewaySecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_gateway_security_group_rule(
        self,
        gateway_id: str,
        request: main_models.AddGatewaySecurityGroupRuleRequest,
    ) -> main_models.AddGatewaySecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_gateway_security_group_rule_with_options(gateway_id, request, headers, runtime)

    async def add_gateway_security_group_rule_async(
        self,
        gateway_id: str,
        request: main_models.AddGatewaySecurityGroupRuleRequest,
    ) -> main_models.AddGatewaySecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_gateway_security_group_rule_with_options_async(gateway_id, request, headers, runtime)

    def batch_add_consumer_group_consumers_with_options(
        self,
        consumer_group_id: str,
        request: main_models.BatchAddConsumerGroupConsumersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddConsumerGroupConsumersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.consumer_ids):
            body['consumerIds'] = request.consumer_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchAddConsumerGroupConsumers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}/consumers/batch-add',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddConsumerGroupConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_consumer_group_consumers_with_options_async(
        self,
        consumer_group_id: str,
        request: main_models.BatchAddConsumerGroupConsumersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddConsumerGroupConsumersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.consumer_ids):
            body['consumerIds'] = request.consumer_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchAddConsumerGroupConsumers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}/consumers/batch-add',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddConsumerGroupConsumersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_consumer_group_consumers(
        self,
        consumer_group_id: str,
        request: main_models.BatchAddConsumerGroupConsumersRequest,
    ) -> main_models.BatchAddConsumerGroupConsumersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_add_consumer_group_consumers_with_options(consumer_group_id, request, headers, runtime)

    async def batch_add_consumer_group_consumers_async(
        self,
        consumer_group_id: str,
        request: main_models.BatchAddConsumerGroupConsumersRequest,
    ) -> main_models.BatchAddConsumerGroupConsumersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_add_consumer_group_consumers_with_options_async(consumer_group_id, request, headers, runtime)

    def batch_delete_consumer_authorization_rule_with_options(
        self,
        request: main_models.BatchDeleteConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteConsumerAuthorizationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_authorization_rule_ids):
            query['consumerAuthorizationRuleIds'] = request.consumer_authorization_rule_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_consumer_authorization_rule_with_options_async(
        self,
        request: main_models.BatchDeleteConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteConsumerAuthorizationRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_authorization_rule_ids):
            query['consumerAuthorizationRuleIds'] = request.consumer_authorization_rule_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_consumer_authorization_rule(
        self,
        request: main_models.BatchDeleteConsumerAuthorizationRuleRequest,
    ) -> main_models.BatchDeleteConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_delete_consumer_authorization_rule_with_options(request, headers, runtime)

    async def batch_delete_consumer_authorization_rule_async(
        self,
        request: main_models.BatchDeleteConsumerAuthorizationRuleRequest,
    ) -> main_models.BatchDeleteConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_delete_consumer_authorization_rule_with_options_async(request, headers, runtime)

    def batch_export_http_apis_with_options(
        self,
        request: main_models.BatchExportHttpApisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchExportHttpApisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_ids):
            body['apiIds'] = request.api_ids
        if not DaraCore.is_null(request.api_type):
            body['apiType'] = request.api_type
        if not DaraCore.is_null(request.extension_config):
            body['extensionConfig'] = request.extension_config
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchExportHttpApis',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/batch-export',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchExportHttpApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_export_http_apis_with_options_async(
        self,
        request: main_models.BatchExportHttpApisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchExportHttpApisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_ids):
            body['apiIds'] = request.api_ids
        if not DaraCore.is_null(request.api_type):
            body['apiType'] = request.api_type
        if not DaraCore.is_null(request.extension_config):
            body['extensionConfig'] = request.extension_config
        if not DaraCore.is_null(request.format):
            body['format'] = request.format
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchExportHttpApis',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/batch-export',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchExportHttpApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_export_http_apis(
        self,
        request: main_models.BatchExportHttpApisRequest,
    ) -> main_models.BatchExportHttpApisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_export_http_apis_with_options(request, headers, runtime)

    async def batch_export_http_apis_async(
        self,
        request: main_models.BatchExportHttpApisRequest,
    ) -> main_models.BatchExportHttpApisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_export_http_apis_with_options_async(request, headers, runtime)

    def batch_import_http_apis_with_options(
        self,
        request: main_models.BatchImportHttpApisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchImportHttpApisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allow_update):
            body['allowUpdate'] = request.allow_update
        if not DaraCore.is_null(request.api_type):
            body['apiType'] = request.api_type
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec_content_base_64):
            body['specContentBase64'] = request.spec_content_base_64
        if not DaraCore.is_null(request.spec_file_url):
            body['specFileUrl'] = request.spec_file_url
        if not DaraCore.is_null(request.spec_oss_config):
            body['specOssConfig'] = request.spec_oss_config
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        if not DaraCore.is_null(request.with_gateway_extension):
            body['withGatewayExtension'] = request.with_gateway_extension
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchImportHttpApis',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/batch-import',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchImportHttpApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_import_http_apis_with_options_async(
        self,
        request: main_models.BatchImportHttpApisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchImportHttpApisResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.allow_update):
            body['allowUpdate'] = request.allow_update
        if not DaraCore.is_null(request.api_type):
            body['apiType'] = request.api_type
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec_content_base_64):
            body['specContentBase64'] = request.spec_content_base_64
        if not DaraCore.is_null(request.spec_file_url):
            body['specFileUrl'] = request.spec_file_url
        if not DaraCore.is_null(request.spec_oss_config):
            body['specOssConfig'] = request.spec_oss_config
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        if not DaraCore.is_null(request.with_gateway_extension):
            body['withGatewayExtension'] = request.with_gateway_extension
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchImportHttpApis',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/batch-import',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchImportHttpApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_import_http_apis(
        self,
        request: main_models.BatchImportHttpApisRequest,
    ) -> main_models.BatchImportHttpApisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_import_http_apis_with_options(request, headers, runtime)

    async def batch_import_http_apis_async(
        self,
        request: main_models.BatchImportHttpApisRequest,
    ) -> main_models.BatchImportHttpApisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_import_http_apis_with_options_async(request, headers, runtime)

    def batch_remove_consumer_group_consumers_with_options(
        self,
        consumer_group_id: str,
        request: main_models.BatchRemoveConsumerGroupConsumersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchRemoveConsumerGroupConsumersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.consumer_ids):
            body['consumerIds'] = request.consumer_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchRemoveConsumerGroupConsumers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}/consumers/batch-remove',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRemoveConsumerGroupConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_remove_consumer_group_consumers_with_options_async(
        self,
        consumer_group_id: str,
        request: main_models.BatchRemoveConsumerGroupConsumersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchRemoveConsumerGroupConsumersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.consumer_ids):
            body['consumerIds'] = request.consumer_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchRemoveConsumerGroupConsumers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}/consumers/batch-remove',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRemoveConsumerGroupConsumersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_remove_consumer_group_consumers(
        self,
        consumer_group_id: str,
        request: main_models.BatchRemoveConsumerGroupConsumersRequest,
    ) -> main_models.BatchRemoveConsumerGroupConsumersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_remove_consumer_group_consumers_with_options(consumer_group_id, request, headers, runtime)

    async def batch_remove_consumer_group_consumers_async(
        self,
        consumer_group_id: str,
        request: main_models.BatchRemoveConsumerGroupConsumersRequest,
    ) -> main_models.BatchRemoveConsumerGroupConsumersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_remove_consumer_group_consumers_with_options_async(consumer_group_id, request, headers, runtime)

    def batch_update_http_api_operation_with_options(
        self,
        http_api_id: str,
        request: main_models.BatchUpdateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateHttpApiOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_config):
            body['authConfig'] = request.auth_config
        if not DaraCore.is_null(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.operation_ids):
            body['operationIds'] = request.operation_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchUpdateHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        request: main_models.BatchUpdateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateHttpApiOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_config):
            body['authConfig'] = request.auth_config
        if not DaraCore.is_null(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.operation_ids):
            body['operationIds'] = request.operation_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchUpdateHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_http_api_operation(
        self,
        http_api_id: str,
        request: main_models.BatchUpdateHttpApiOperationRequest,
    ) -> main_models.BatchUpdateHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_update_http_api_operation_with_options(http_api_id, request, headers, runtime)

    async def batch_update_http_api_operation_async(
        self,
        http_api_id: str,
        request: main_models.BatchUpdateHttpApiOperationRequest,
    ) -> main_models.BatchUpdateHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_update_http_api_operation_with_options_async(http_api_id, request, headers, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/move-resource-group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/move-resource-group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_ai_model_card_with_options(
        self,
        request: main_models.CreateAiModelCardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAiModelCardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.available_paths):
            body['availablePaths'] = request.available_paths
        if not DaraCore.is_null(request.credit):
            body['credit'] = request.credit
        if not DaraCore.is_null(request.features):
            body['features'] = request.features
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.meta):
            body['meta'] = request.meta
        if not DaraCore.is_null(request.model_name):
            body['modelName'] = request.model_name
        if not DaraCore.is_null(request.model_provider):
            body['modelProvider'] = request.model_provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAiModelCard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-cards',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAiModelCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_model_card_with_options_async(
        self,
        request: main_models.CreateAiModelCardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAiModelCardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.available_paths):
            body['availablePaths'] = request.available_paths
        if not DaraCore.is_null(request.credit):
            body['credit'] = request.credit
        if not DaraCore.is_null(request.features):
            body['features'] = request.features
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.meta):
            body['meta'] = request.meta
        if not DaraCore.is_null(request.model_name):
            body['modelName'] = request.model_name
        if not DaraCore.is_null(request.model_provider):
            body['modelProvider'] = request.model_provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAiModelCard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-cards',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAiModelCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_model_card(
        self,
        request: main_models.CreateAiModelCardRequest,
    ) -> main_models.CreateAiModelCardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_ai_model_card_with_options(request, headers, runtime)

    async def create_ai_model_card_async(
        self,
        request: main_models.CreateAiModelCardRequest,
    ) -> main_models.CreateAiModelCardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_ai_model_card_with_options_async(request, headers, runtime)

    def create_ai_model_provider_with_options(
        self,
        request: main_models.CreateAiModelProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAiModelProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.provider):
            body['provider'] = request.provider
        if not DaraCore.is_null(request.service_ids):
            body['serviceIds'] = request.service_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAiModelProvider',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-providers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAiModelProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ai_model_provider_with_options_async(
        self,
        request: main_models.CreateAiModelProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAiModelProviderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.provider):
            body['provider'] = request.provider
        if not DaraCore.is_null(request.service_ids):
            body['serviceIds'] = request.service_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAiModelProvider',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-providers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAiModelProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ai_model_provider(
        self,
        request: main_models.CreateAiModelProviderRequest,
    ) -> main_models.CreateAiModelProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_ai_model_provider_with_options(request, headers, runtime)

    async def create_ai_model_provider_async(
        self,
        request: main_models.CreateAiModelProviderRequest,
    ) -> main_models.CreateAiModelProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_ai_model_provider_with_options_async(request, headers, runtime)

    def create_and_attach_policy_with_options(
        self,
        request: main_models.CreateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndAttachPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.class_name):
            body['className'] = request.class_name
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndAttachPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndAttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_attach_policy_with_options_async(
        self,
        request: main_models.CreateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndAttachPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.class_name):
            body['className'] = request.class_name
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndAttachPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndAttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_attach_policy(
        self,
        request: main_models.CreateAndAttachPolicyRequest,
    ) -> main_models.CreateAndAttachPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_and_attach_policy_with_options(request, headers, runtime)

    async def create_and_attach_policy_async(
        self,
        request: main_models.CreateAndAttachPolicyRequest,
    ) -> main_models.CreateAndAttachPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_and_attach_policy_with_options_async(request, headers, runtime)

    def create_consumer_with_options(
        self,
        request: main_models.CreateConsumerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not DaraCore.is_null(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_with_options_async(
        self,
        request: main_models.CreateConsumerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not DaraCore.is_null(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer(
        self,
        request: main_models.CreateConsumerRequest,
    ) -> main_models.CreateConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_consumer_with_options(request, headers, runtime)

    async def create_consumer_async(
        self,
        request: main_models.CreateConsumerRequest,
    ) -> main_models.CreateConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_consumer_with_options_async(request, headers, runtime)

    def create_consumer_authorization_rule_with_options(
        self,
        consumer_id: str,
        request: main_models.CreateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerAuthorizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not DaraCore.is_null(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not DaraCore.is_null(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        if not DaraCore.is_null(request.parent_resource_type):
            body['parentResourceType'] = request.parent_resource_type
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_authorization_rule_with_options_async(
        self,
        consumer_id: str,
        request: main_models.CreateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerAuthorizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not DaraCore.is_null(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not DaraCore.is_null(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        if not DaraCore.is_null(request.parent_resource_type):
            body['parentResourceType'] = request.parent_resource_type
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_authorization_rule(
        self,
        consumer_id: str,
        request: main_models.CreateConsumerAuthorizationRuleRequest,
    ) -> main_models.CreateConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_consumer_authorization_rule_with_options(consumer_id, request, headers, runtime)

    async def create_consumer_authorization_rule_async(
        self,
        consumer_id: str,
        request: main_models.CreateConsumerAuthorizationRuleRequest,
    ) -> main_models.CreateConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_consumer_authorization_rule_with_options_async(consumer_id, request, headers, runtime)

    def create_consumer_authorization_rules_with_options(
        self,
        request: main_models.CreateConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerAuthorizationRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_rules):
            body['authorizationRules'] = request.authorization_rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerAuthorizationRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_authorization_rules_with_options_async(
        self,
        request: main_models.CreateConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerAuthorizationRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_rules):
            body['authorizationRules'] = request.authorization_rules
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerAuthorizationRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerAuthorizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_authorization_rules(
        self,
        request: main_models.CreateConsumerAuthorizationRulesRequest,
    ) -> main_models.CreateConsumerAuthorizationRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_consumer_authorization_rules_with_options(request, headers, runtime)

    async def create_consumer_authorization_rules_async(
        self,
        request: main_models.CreateConsumerAuthorizationRulesRequest,
    ) -> main_models.CreateConsumerAuthorizationRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_consumer_authorization_rules_with_options_async(request, headers, runtime)

    def create_consumer_group_with_options(
        self,
        request: main_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.consumer_group_id):
            body['consumerGroupId'] = request.consumer_group_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: main_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.consumer_group_id):
            body['consumerGroupId'] = request.consumer_group_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_group(
        self,
        request: main_models.CreateConsumerGroupRequest,
    ) -> main_models.CreateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(request, headers, runtime)

    async def create_consumer_group_async(
        self,
        request: main_models.CreateConsumerGroupRequest,
    ) -> main_models.CreateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_consumer_group_with_options_async(request, headers, runtime)

    def create_domain_with_options(
        self,
        request: main_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not DaraCore.is_null(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not DaraCore.is_null(request.domain_scope):
            body['domainScope'] = request.domain_scope
        if not DaraCore.is_null(request.force_https):
            body['forceHttps'] = request.force_https
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.http_2option):
            body['http2Option'] = request.http_2option
        if not DaraCore.is_null(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not DaraCore.is_null(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: main_models.CreateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not DaraCore.is_null(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not DaraCore.is_null(request.domain_scope):
            body['domainScope'] = request.domain_scope
        if not DaraCore.is_null(request.force_https):
            body['forceHttps'] = request.force_https
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.http_2option):
            body['http2Option'] = request.http_2option
        if not DaraCore.is_null(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not DaraCore.is_null(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.create_domain_with_options(request, headers, runtime)

    async def create_domain_async(
        self,
        request: main_models.CreateDomainRequest,
    ) -> main_models.CreateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_domain_with_options_async(request, headers, runtime)

    def create_environment_with_options(
        self,
        request: main_models.CreateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvironmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_environment_with_options_async(
        self,
        request: main_models.CreateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvironmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_environment(
        self,
        request: main_models.CreateEnvironmentRequest,
    ) -> main_models.CreateEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_environment_with_options(request, headers, runtime)

    async def create_environment_async(
        self,
        request: main_models.CreateEnvironmentRequest,
    ) -> main_models.CreateEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_environment_with_options_async(request, headers, runtime)

    def create_gateway_with_options(
        self,
        request: main_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.charge_type):
            body['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.gateway_edition):
            body['gatewayEdition'] = request.gateway_edition
        if not DaraCore.is_null(request.gateway_mode):
            body['gatewayMode'] = request.gateway_mode
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.log_config):
            body['logConfig'] = request.log_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.network_access_config):
            body['networkAccessConfig'] = request.network_access_config
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec):
            body['spec'] = request.spec
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_config):
            body['zoneConfig'] = request.zone_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_with_options_async(
        self,
        request: main_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGatewayResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.charge_type):
            body['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.gateway_edition):
            body['gatewayEdition'] = request.gateway_edition
        if not DaraCore.is_null(request.gateway_mode):
            body['gatewayMode'] = request.gateway_mode
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.log_config):
            body['logConfig'] = request.log_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.network_access_config):
            body['networkAccessConfig'] = request.network_access_config
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec):
            body['spec'] = request.spec
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_config):
            body['zoneConfig'] = request.zone_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway(
        self,
        request: main_models.CreateGatewayRequest,
    ) -> main_models.CreateGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_gateway_with_options(request, headers, runtime)

    async def create_gateway_async(
        self,
        request: main_models.CreateGatewayRequest,
    ) -> main_models.CreateGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_gateway_with_options_async(request, headers, runtime)

    def create_http_api_with_options(
        self,
        request: main_models.CreateHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not DaraCore.is_null(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not DaraCore.is_null(request.auth_config):
            body['authConfig'] = request.auth_config
        if not DaraCore.is_null(request.base_path):
            body['basePath'] = request.base_path
        if not DaraCore.is_null(request.belong_gateway_id):
            body['belongGatewayId'] = request.belong_gateway_id
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not DaraCore.is_null(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not DaraCore.is_null(request.model_category):
            body['modelCategory'] = request.model_category
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocols):
            body['protocols'] = request.protocols
        if not DaraCore.is_null(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_with_options_async(
        self,
        request: main_models.CreateHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not DaraCore.is_null(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not DaraCore.is_null(request.auth_config):
            body['authConfig'] = request.auth_config
        if not DaraCore.is_null(request.base_path):
            body['basePath'] = request.base_path
        if not DaraCore.is_null(request.belong_gateway_id):
            body['belongGatewayId'] = request.belong_gateway_id
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not DaraCore.is_null(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not DaraCore.is_null(request.model_category):
            body['modelCategory'] = request.model_category
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocols):
            body['protocols'] = request.protocols
        if not DaraCore.is_null(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api(
        self,
        request: main_models.CreateHttpApiRequest,
    ) -> main_models.CreateHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_http_api_with_options(request, headers, runtime)

    async def create_http_api_async(
        self,
        request: main_models.CreateHttpApiRequest,
    ) -> main_models.CreateHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_http_api_with_options_async(request, headers, runtime)

    def create_http_api_operation_with_options(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operations):
            body['operations'] = request.operations
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operations):
            body['operations'] = request.operations
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api_operation(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiOperationRequest,
    ) -> main_models.CreateHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_http_api_operation_with_options(http_api_id, request, headers, runtime)

    async def create_http_api_operation_async(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiOperationRequest,
    ) -> main_models.CreateHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_http_api_operation_with_options_async(http_api_id, request, headers, runtime)

    def create_http_api_route_with_options(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.policy_configs):
            body['policyConfigs'] = request.policy_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_route_with_options_async(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.policy_configs):
            body['policyConfigs'] = request.policy_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api_route(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiRouteRequest,
    ) -> main_models.CreateHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_http_api_route_with_options(http_api_id, request, headers, runtime)

    async def create_http_api_route_async(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiRouteRequest,
    ) -> main_models.CreateHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_http_api_route_with_options_async(http_api_id, request, headers, runtime)

    def create_http_api_version_with_options(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApiVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_http_api_version_with_options_async(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHttpApiVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHttpApiVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHttpApiVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_http_api_version(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiVersionRequest,
    ) -> main_models.CreateHttpApiVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_http_api_version_with_options(http_api_id, request, headers, runtime)

    async def create_http_api_version_async(
        self,
        http_api_id: str,
        request: main_models.CreateHttpApiVersionRequest,
    ) -> main_models.CreateHttpApiVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_http_api_version_with_options_async(http_api_id, request, headers, runtime)

    def create_mcp_server_with_options(
        self,
        request: main_models.CreateMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcpServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.create_from_type):
            body['createFromType'] = request.create_from_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gray_mcp_server_configs):
            body['grayMcpServerConfigs'] = request.gray_mcp_server_configs
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_server_config):
            body['mcpServerConfig'] = request.mcp_server_config
        if not DaraCore.is_null(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mcp_server_with_options_async(
        self,
        request: main_models.CreateMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMcpServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.create_from_type):
            body['createFromType'] = request.create_from_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gray_mcp_server_configs):
            body['grayMcpServerConfigs'] = request.gray_mcp_server_configs
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_server_config):
            body['mcpServerConfig'] = request.mcp_server_config
        if not DaraCore.is_null(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mcp_server(
        self,
        request: main_models.CreateMcpServerRequest,
    ) -> main_models.CreateMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_mcp_server_with_options(request, headers, runtime)

    async def create_mcp_server_async(
        self,
        request: main_models.CreateMcpServerRequest,
    ) -> main_models.CreateMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_mcp_server_with_options_async(request, headers, runtime)

    def create_migration_task_with_options(
        self,
        request: main_models.CreateMigrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMigrationTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.http_api_id):
            body['httpApiId'] = request.http_api_id
        if not DaraCore.is_null(request.ingress_class):
            body['ingressClass'] = request.ingress_class
        if not DaraCore.is_null(request.migration_type):
            body['migrationType'] = request.migration_type
        if not DaraCore.is_null(request.watch_namespace):
            body['watchNamespace'] = request.watch_namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMigrationTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_migration_task_with_options_async(
        self,
        request: main_models.CreateMigrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMigrationTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['clusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.http_api_id):
            body['httpApiId'] = request.http_api_id
        if not DaraCore.is_null(request.ingress_class):
            body['ingressClass'] = request.ingress_class
        if not DaraCore.is_null(request.migration_type):
            body['migrationType'] = request.migration_type
        if not DaraCore.is_null(request.watch_namespace):
            body['watchNamespace'] = request.watch_namespace
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMigrationTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMigrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_migration_task(
        self,
        request: main_models.CreateMigrationTaskRequest,
    ) -> main_models.CreateMigrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_migration_task_with_options(request, headers, runtime)

    async def create_migration_task_async(
        self,
        request: main_models.CreateMigrationTaskRequest,
    ) -> main_models.CreateMigrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_migration_task_with_options_async(request, headers, runtime)

    def create_plugin_attachment_with_options(
        self,
        request: main_models.CreatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        if not DaraCore.is_null(request.plugin_id):
            body['pluginId'] = request.plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_plugin_attachment_with_options_async(
        self,
        request: main_models.CreatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        if not DaraCore.is_null(request.plugin_id):
            body['pluginId'] = request.plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_plugin_attachment(
        self,
        request: main_models.CreatePluginAttachmentRequest,
    ) -> main_models.CreatePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_plugin_attachment_with_options(request, headers, runtime)

    async def create_plugin_attachment_async(
        self,
        request: main_models.CreatePluginAttachmentRequest,
    ) -> main_models.CreatePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_plugin_attachment_with_options_async(request, headers, runtime)

    def create_plugin_class_with_options(
        self,
        request: main_models.CreatePluginClassRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginClassResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.execute_priority):
            body['executePriority'] = request.execute_priority
        if not DaraCore.is_null(request.execute_stage):
            body['executeStage'] = request.execute_stage
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.supported_min_gateway_version):
            body['supportedMinGatewayVersion'] = request.supported_min_gateway_version
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.version_description):
            body['versionDescription'] = request.version_description
        if not DaraCore.is_null(request.wasm_language):
            body['wasmLanguage'] = request.wasm_language
        if not DaraCore.is_null(request.wasm_url):
            body['wasmUrl'] = request.wasm_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePluginClass',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-classes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_plugin_class_with_options_async(
        self,
        request: main_models.CreatePluginClassRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginClassResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.execute_priority):
            body['executePriority'] = request.execute_priority
        if not DaraCore.is_null(request.execute_stage):
            body['executeStage'] = request.execute_stage
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.supported_min_gateway_version):
            body['supportedMinGatewayVersion'] = request.supported_min_gateway_version
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.version_description):
            body['versionDescription'] = request.version_description
        if not DaraCore.is_null(request.wasm_language):
            body['wasmLanguage'] = request.wasm_language
        if not DaraCore.is_null(request.wasm_url):
            body['wasmUrl'] = request.wasm_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePluginClass',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-classes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_plugin_class(
        self,
        request: main_models.CreatePluginClassRequest,
    ) -> main_models.CreatePluginClassResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_plugin_class_with_options(request, headers, runtime)

    async def create_plugin_class_async(
        self,
        request: main_models.CreatePluginClassRequest,
    ) -> main_models.CreatePluginClassResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_plugin_class_with_options_async(request, headers, runtime)

    def create_plugin_workspace_with_options(
        self,
        request: main_models.CreatePluginWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.organization_id):
            body['organizationId'] = request.organization_id
        if not DaraCore.is_null(request.repo_name):
            body['repoName'] = request.repo_name
        if not DaraCore.is_null(request.workspace_name):
            body['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePluginWorkspace',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_plugin_workspace_with_options_async(
        self,
        request: main_models.CreatePluginWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePluginWorkspaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.organization_id):
            body['organizationId'] = request.organization_id
        if not DaraCore.is_null(request.repo_name):
            body['repoName'] = request.repo_name
        if not DaraCore.is_null(request.workspace_name):
            body['workspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePluginWorkspace',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-workspaces',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePluginWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_plugin_workspace(
        self,
        request: main_models.CreatePluginWorkspaceRequest,
    ) -> main_models.CreatePluginWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_plugin_workspace_with_options(request, headers, runtime)

    async def create_plugin_workspace_async(
        self,
        request: main_models.CreatePluginWorkspaceRequest,
    ) -> main_models.CreatePluginWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_plugin_workspace_with_options_async(request, headers, runtime)

    def create_policy_with_options(
        self,
        request: main_models.CreatePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.class_name):
            body['className'] = request.class_name
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: main_models.CreatePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.class_name):
            body['className'] = request.class_name
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_policy_with_options(request, headers, runtime)

    async def create_policy_async(
        self,
        request: main_models.CreatePolicyRequest,
    ) -> main_models.CreatePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_policy_with_options_async(request, headers, runtime)

    def create_policy_attachment_with_options(
        self,
        request: main_models.CreatePolicyAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_id):
            body['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.policy_id):
            body['policyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_attachment_with_options_async(
        self,
        request: main_models.CreatePolicyAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_id):
            body['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.policy_id):
            body['policyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_attachment(
        self,
        request: main_models.CreatePolicyAttachmentRequest,
    ) -> main_models.CreatePolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_policy_attachment_with_options(request, headers, runtime)

    async def create_policy_attachment_async(
        self,
        request: main_models.CreatePolicyAttachmentRequest,
    ) -> main_models.CreatePolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_policy_attachment_with_options_async(request, headers, runtime)

    def create_risk_check_task_with_options(
        self,
        gateway_id: str,
        request: main_models.CreateRiskCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRiskCheckTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateRiskCheckTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/risk-check/tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRiskCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_risk_check_task_with_options_async(
        self,
        gateway_id: str,
        request: main_models.CreateRiskCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRiskCheckTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateRiskCheckTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/risk-check/tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRiskCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_risk_check_task(
        self,
        gateway_id: str,
        request: main_models.CreateRiskCheckTaskRequest,
    ) -> main_models.CreateRiskCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_risk_check_task_with_options(gateway_id, request, headers, runtime)

    async def create_risk_check_task_async(
        self,
        gateway_id: str,
        request: main_models.CreateRiskCheckTaskRequest,
    ) -> main_models.CreateRiskCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_risk_check_task_with_options_async(gateway_id, request, headers, runtime)

    def create_secret_with_options(
        self,
        request: main_models.CreateSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.kms_config):
            body['kmsConfig'] = request.kms_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.secret_data):
            body['secretData'] = request.secret_data
        if not DaraCore.is_null(request.secret_source):
            body['secretSource'] = request.secret_source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecret',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_with_options_async(
        self,
        request: main_models.CreateSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.kms_config):
            body['kmsConfig'] = request.kms_config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.secret_data):
            body['secretData'] = request.secret_data
        if not DaraCore.is_null(request.secret_source):
            body['secretSource'] = request.secret_source
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecret',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret(
        self,
        request: main_models.CreateSecretRequest,
    ) -> main_models.CreateSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_secret_with_options(request, headers, runtime)

    async def create_secret_async(
        self,
        request: main_models.CreateSecretRequest,
    ) -> main_models.CreateSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_secret_with_options_async(request, headers, runtime)

    def create_service_with_options(
        self,
        request: main_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_configs):
            body['serviceConfigs'] = request.service_configs
        if not DaraCore.is_null(request.source_type):
            body['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: main_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_configs):
            body['serviceConfigs'] = request.service_configs
        if not DaraCore.is_null(request.source_type):
            body['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: main_models.CreateServiceRequest,
    ) -> main_models.CreateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    async def create_service_async(
        self,
        request: main_models.CreateServiceRequest,
    ) -> main_models.CreateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(request, headers, runtime)

    def create_service_version_with_options(
        self,
        service_id: str,
        request: main_models.CreateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_version_with_options_async(
        self,
        service_id: str,
        request: main_models.CreateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['labels'] = request.labels
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_version(
        self,
        service_id: str,
        request: main_models.CreateServiceVersionRequest,
    ) -> main_models.CreateServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_service_version_with_options(service_id, request, headers, runtime)

    async def create_service_version_async(
        self,
        service_id: str,
        request: main_models.CreateServiceVersionRequest,
    ) -> main_models.CreateServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_service_version_with_options_async(service_id, request, headers, runtime)

    def create_source_with_options(
        self,
        request: main_models.CreateSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.k_8s_source_config):
            body['k8sSourceConfig'] = request.k_8s_source_config
        if not DaraCore.is_null(request.nacos_source_config):
            body['nacosSourceConfig'] = request.nacos_source_config
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_source_with_options_async(
        self,
        request: main_models.CreateSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.k_8s_source_config):
            body['k8sSourceConfig'] = request.k_8s_source_config
        if not DaraCore.is_null(request.nacos_source_config):
            body['nacosSourceConfig'] = request.nacos_source_config
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_source(
        self,
        request: main_models.CreateSourceRequest,
    ) -> main_models.CreateSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_source_with_options(request, headers, runtime)

    async def create_source_async(
        self,
        request: main_models.CreateSourceRequest,
    ) -> main_models.CreateSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_source_with_options_async(request, headers, runtime)

    def delete_ai_model_card_with_options(
        self,
        model_card_id: str,
        request: main_models.DeleteAiModelCardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAiModelCardResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAiModelCard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-cards/{DaraURL.percent_encode(model_card_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAiModelCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ai_model_card_with_options_async(
        self,
        model_card_id: str,
        request: main_models.DeleteAiModelCardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAiModelCardResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAiModelCard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-cards/{DaraURL.percent_encode(model_card_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAiModelCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ai_model_card(
        self,
        model_card_id: str,
        request: main_models.DeleteAiModelCardRequest,
    ) -> main_models.DeleteAiModelCardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_ai_model_card_with_options(model_card_id, request, headers, runtime)

    async def delete_ai_model_card_async(
        self,
        model_card_id: str,
        request: main_models.DeleteAiModelCardRequest,
    ) -> main_models.DeleteAiModelCardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_ai_model_card_with_options_async(model_card_id, request, headers, runtime)

    def delete_ai_model_provider_with_options(
        self,
        model_provider_id: str,
        request: main_models.DeleteAiModelProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAiModelProviderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAiModelProvider',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-providers/{DaraURL.percent_encode(model_provider_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAiModelProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ai_model_provider_with_options_async(
        self,
        model_provider_id: str,
        request: main_models.DeleteAiModelProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAiModelProviderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAiModelProvider',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-providers/{DaraURL.percent_encode(model_provider_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAiModelProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ai_model_provider(
        self,
        model_provider_id: str,
        request: main_models.DeleteAiModelProviderRequest,
    ) -> main_models.DeleteAiModelProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_ai_model_provider_with_options(model_provider_id, request, headers, runtime)

    async def delete_ai_model_provider_async(
        self,
        model_provider_id: str,
        request: main_models.DeleteAiModelProviderRequest,
    ) -> main_models.DeleteAiModelProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_ai_model_provider_with_options_async(model_provider_id, request, headers, runtime)

    def delete_consumer_with_options(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_with_options_async(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer(
        self,
        consumer_id: str,
    ) -> main_models.DeleteConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_consumer_with_options(consumer_id, headers, runtime)

    async def delete_consumer_async(
        self,
        consumer_id: str,
    ) -> main_models.DeleteConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_consumer_with_options_async(consumer_id, headers, runtime)

    def delete_consumer_authorization_rule_with_options(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_authorization_rule_with_options_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_authorization_rule(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> main_models.DeleteConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_consumer_authorization_rule_with_options(consumer_authorization_rule_id, consumer_id, headers, runtime)

    async def delete_consumer_authorization_rule_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> main_models.DeleteConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_consumer_authorization_rule_with_options_async(consumer_authorization_rule_id, consumer_id, headers, runtime)

    def delete_consumer_group_with_options(
        self,
        consumer_group_id: str,
        request: main_models.DeleteConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        consumer_group_id: str,
        request: main_models.DeleteConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_group(
        self,
        consumer_group_id: str,
        request: main_models.DeleteConsumerGroupRequest,
    ) -> main_models.DeleteConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(consumer_group_id, request, headers, runtime)

    async def delete_consumer_group_async(
        self,
        consumer_group_id: str,
        request: main_models.DeleteConsumerGroupRequest,
    ) -> main_models.DeleteConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_consumer_group_with_options_async(consumer_group_id, request, headers, runtime)

    def delete_domain_with_options(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        domain_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDomainResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        domain_id: str,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_domain_with_options(domain_id, headers, runtime)

    async def delete_domain_async(
        self,
        domain_id: str,
    ) -> main_models.DeleteDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_domain_with_options_async(domain_id, headers, runtime)

    def delete_environment_with_options(
        self,
        environment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvironmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_with_options_async(
        self,
        environment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvironmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment(
        self,
        environment_id: str,
    ) -> main_models.DeleteEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_environment_with_options(environment_id, headers, runtime)

    async def delete_environment_async(
        self,
        environment_id: str,
    ) -> main_models.DeleteEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_environment_with_options_async(environment_id, headers, runtime)

    def delete_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway(
        self,
        gateway_id: str,
    ) -> main_models.DeleteGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_gateway_with_options(gateway_id, headers, runtime)

    async def delete_gateway_async(
        self,
        gateway_id: str,
    ) -> main_models.DeleteGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_gateway_with_options_async(gateway_id, headers, runtime)

    def delete_gateway_quota_rule_with_options(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.DeleteGatewayQuotaRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayQuotaRuleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayQuotaRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayQuotaRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_quota_rule_with_options_async(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.DeleteGatewayQuotaRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewayQuotaRuleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewayQuotaRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewayQuotaRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_quota_rule(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.DeleteGatewayQuotaRuleRequest,
    ) -> main_models.DeleteGatewayQuotaRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_gateway_quota_rule_with_options(gateway_id, rule_id, request, headers, runtime)

    async def delete_gateway_quota_rule_async(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.DeleteGatewayQuotaRuleRequest,
    ) -> main_models.DeleteGatewayQuotaRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_gateway_quota_rule_with_options_async(gateway_id, rule_id, request, headers, runtime)

    def delete_gateway_security_group_rule_with_options(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: main_models.DeleteGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewaySecurityGroupRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cascading_delete):
            query['cascadingDelete'] = request.cascading_delete
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewaySecurityGroupRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/security-group-rules/{DaraURL.percent_encode(security_group_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewaySecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_security_group_rule_with_options_async(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: main_models.DeleteGatewaySecurityGroupRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGatewaySecurityGroupRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cascading_delete):
            query['cascadingDelete'] = request.cascading_delete
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGatewaySecurityGroupRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/security-group-rules/{DaraURL.percent_encode(security_group_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGatewaySecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_security_group_rule(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: main_models.DeleteGatewaySecurityGroupRuleRequest,
    ) -> main_models.DeleteGatewaySecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_gateway_security_group_rule_with_options(gateway_id, security_group_rule_id, request, headers, runtime)

    async def delete_gateway_security_group_rule_async(
        self,
        gateway_id: str,
        security_group_rule_id: str,
        request: main_models.DeleteGatewaySecurityGroupRuleRequest,
    ) -> main_models.DeleteGatewaySecurityGroupRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_gateway_security_group_rule_with_options_async(gateway_id, security_group_rule_id, request, headers, runtime)

    def delete_http_api_with_options(
        self,
        http_api_id: str,
        request: main_models.DeleteHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_with_options_async(
        self,
        http_api_id: str,
        request: main_models.DeleteHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api(
        self,
        http_api_id: str,
        request: main_models.DeleteHttpApiRequest,
    ) -> main_models.DeleteHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_http_api_with_options(http_api_id, request, headers, runtime)

    async def delete_http_api_async(
        self,
        http_api_id: str,
        request: main_models.DeleteHttpApiRequest,
    ) -> main_models.DeleteHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_http_api_with_options_async(http_api_id, request, headers, runtime)

    def delete_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiOperationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiOperationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> main_models.DeleteHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_http_api_operation_with_options(http_api_id, operation_id, headers, runtime)

    async def delete_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> main_models.DeleteHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_http_api_operation_with_options_async(http_api_id, operation_id, headers, runtime)

    def delete_http_api_route_with_options(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiRouteResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_http_api_route_with_options_async(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHttpApiRouteResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_http_api_route(
        self,
        http_api_id: str,
        route_id: str,
    ) -> main_models.DeleteHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_http_api_route_with_options(http_api_id, route_id, headers, runtime)

    async def delete_http_api_route_async(
        self,
        http_api_id: str,
        route_id: str,
    ) -> main_models.DeleteHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_http_api_route_with_options_async(http_api_id, route_id, headers, runtime)

    def delete_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mcp_server(
        self,
        mcp_server_id: str,
    ) -> main_models.DeleteMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def delete_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> main_models.DeleteMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def delete_migration_task_with_options(
        self,
        task_id: str,
        request: main_models.DeleteMigrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMigrationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMigrationTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_migration_task_with_options_async(
        self,
        task_id: str,
        request: main_models.DeleteMigrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMigrationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMigrationTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMigrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_migration_task(
        self,
        task_id: str,
        request: main_models.DeleteMigrationTaskRequest,
    ) -> main_models.DeleteMigrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_migration_task_with_options(task_id, request, headers, runtime)

    async def delete_migration_task_async(
        self,
        task_id: str,
        request: main_models.DeleteMigrationTaskRequest,
    ) -> main_models.DeleteMigrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_migration_task_with_options_async(task_id, request, headers, runtime)

    def delete_plugin_attachment_with_options(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePluginAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_plugin_attachment_with_options_async(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePluginAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_plugin_attachment(
        self,
        plugin_attachment_id: str,
    ) -> main_models.DeletePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_plugin_attachment_with_options(plugin_attachment_id, headers, runtime)

    async def delete_plugin_attachment_async(
        self,
        plugin_attachment_id: str,
    ) -> main_models.DeletePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_plugin_attachment_with_options_async(plugin_attachment_id, headers, runtime)

    def delete_plugin_class_with_options(
        self,
        plugin_class_id: str,
        request: main_models.DeletePluginClassRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePluginClassResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePluginClass',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-classes/{DaraURL.percent_encode(plugin_class_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePluginClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_plugin_class_with_options_async(
        self,
        plugin_class_id: str,
        request: main_models.DeletePluginClassRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePluginClassResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePluginClass',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-classes/{DaraURL.percent_encode(plugin_class_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePluginClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_plugin_class(
        self,
        plugin_class_id: str,
        request: main_models.DeletePluginClassRequest,
    ) -> main_models.DeletePluginClassResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_plugin_class_with_options(plugin_class_id, request, headers, runtime)

    async def delete_plugin_class_async(
        self,
        plugin_class_id: str,
        request: main_models.DeletePluginClassRequest,
    ) -> main_models.DeletePluginClassResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_plugin_class_with_options_async(plugin_class_id, request, headers, runtime)

    def delete_policy_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        policy_id: str,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_policy_with_options(policy_id, headers, runtime)

    async def delete_policy_async(
        self,
        policy_id: str,
    ) -> main_models.DeletePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_policy_with_options_async(policy_id, headers, runtime)

    def delete_policy_attachment_with_options(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments/{DaraURL.percent_encode(policy_attachment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_attachment_with_options_async(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments/{DaraURL.percent_encode(policy_attachment_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_attachment(
        self,
        policy_attachment_id: str,
    ) -> main_models.DeletePolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_policy_attachment_with_options(policy_attachment_id, headers, runtime)

    async def delete_policy_attachment_async(
        self,
        policy_attachment_id: str,
    ) -> main_models.DeletePolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_policy_attachment_with_options_async(policy_attachment_id, headers, runtime)

    def delete_secret_with_options(
        self,
        secret_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecret',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets/{DaraURL.percent_encode(secret_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_with_options_async(
        self,
        secret_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecret',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets/{DaraURL.percent_encode(secret_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret(
        self,
        secret_id: str,
    ) -> main_models.DeleteSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_secret_with_options(secret_id, headers, runtime)

    async def delete_secret_async(
        self,
        secret_id: str,
    ) -> main_models.DeleteSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_secret_with_options_async(secret_id, headers, runtime)

    def delete_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        service_id: str,
    ) -> main_models.DeleteServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(service_id, headers, runtime)

    async def delete_service_async(
        self,
        service_id: str,
    ) -> main_models.DeleteServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(service_id, headers, runtime)

    def delete_service_version_with_options(
        self,
        service_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_version_with_options_async(
        self,
        service_id: str,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions/{DaraURL.percent_encode(name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_version(
        self,
        service_id: str,
        name: str,
    ) -> main_models.DeleteServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_service_version_with_options(service_id, name, headers, runtime)

    async def delete_service_version_async(
        self,
        service_id: str,
        name: str,
    ) -> main_models.DeleteServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_service_version_with_options_async(service_id, name, headers, runtime)

    def delete_source_with_options(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources/{DaraURL.percent_encode(source_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_source_with_options_async(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources/{DaraURL.percent_encode(source_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_source(
        self,
        source_id: str,
    ) -> main_models.DeleteSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_source_with_options(source_id, headers, runtime)

    async def delete_source_async(
        self,
        source_id: str,
    ) -> main_models.DeleteSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_source_with_options_async(source_id, headers, runtime)

    def deploy_http_api_with_options(
        self,
        http_api_id: str,
        request: main_models.DeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.http_api_config):
            body['httpApiConfig'] = request.http_api_config
        if not DaraCore.is_null(request.rest_api_config):
            body['restApiConfig'] = request.rest_api_config
        if not DaraCore.is_null(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeployHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_http_api_with_options_async(
        self,
        http_api_id: str,
        request: main_models.DeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.http_api_config):
            body['httpApiConfig'] = request.http_api_config
        if not DaraCore.is_null(request.rest_api_config):
            body['restApiConfig'] = request.rest_api_config
        if not DaraCore.is_null(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeployHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_http_api(
        self,
        http_api_id: str,
        request: main_models.DeployHttpApiRequest,
    ) -> main_models.DeployHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.deploy_http_api_with_options(http_api_id, request, headers, runtime)

    async def deploy_http_api_async(
        self,
        http_api_id: str,
        request: main_models.DeployHttpApiRequest,
    ) -> main_models.DeployHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.deploy_http_api_with_options_async(http_api_id, request, headers, runtime)

    def deploy_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeployMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}/deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeployMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeployMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}/deploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_mcp_server(
        self,
        mcp_server_id: str,
    ) -> main_models.DeployMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.deploy_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def deploy_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> main_models.DeployMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.deploy_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/regions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['language'] = request.language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/regions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def detach_and_delete_policy_with_options(
        self,
        policy_id: str,
        request: main_models.DetachAndDeletePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DetachAndDeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_attachment_id):
            query['policyAttachmentId'] = request.policy_attachment_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachAndDeletePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachAndDeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_and_delete_policy_with_options_async(
        self,
        policy_id: str,
        request: main_models.DetachAndDeletePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DetachAndDeletePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.policy_attachment_id):
            query['policyAttachmentId'] = request.policy_attachment_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachAndDeletePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachAndDeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_and_delete_policy(
        self,
        policy_id: str,
        request: main_models.DetachAndDeletePolicyRequest,
    ) -> main_models.DetachAndDeletePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.detach_and_delete_policy_with_options(policy_id, request, headers, runtime)

    async def detach_and_delete_policy_async(
        self,
        policy_id: str,
        request: main_models.DetachAndDeletePolicyRequest,
    ) -> main_models.DetachAndDeletePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.detach_and_delete_policy_with_options_async(policy_id, request, headers, runtime)

    def export_http_api_with_options(
        self,
        http_api_id: str,
        request: main_models.ExportHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExportHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extension_config):
            body['extensionConfig'] = request.extension_config
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.operation_ids):
            body['operationIds'] = request.operation_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/export',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_http_api_with_options_async(
        self,
        http_api_id: str,
        request: main_models.ExportHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExportHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.extension_config):
            body['extensionConfig'] = request.extension_config
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.operation_ids):
            body['operationIds'] = request.operation_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/export',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_http_api(
        self,
        http_api_id: str,
        request: main_models.ExportHttpApiRequest,
    ) -> main_models.ExportHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.export_http_api_with_options(http_api_id, request, headers, runtime)

    async def export_http_api_async(
        self,
        http_api_id: str,
        request: main_models.ExportHttpApiRequest,
    ) -> main_models.ExportHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.export_http_api_with_options_async(http_api_id, request, headers, runtime)

    def get_ai_model_card_with_options(
        self,
        model_card_id: str,
        request: main_models.GetAiModelCardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAiModelCardResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAiModelCard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-cards/{DaraURL.percent_encode(model_card_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiModelCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_model_card_with_options_async(
        self,
        model_card_id: str,
        request: main_models.GetAiModelCardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAiModelCardResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAiModelCard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-cards/{DaraURL.percent_encode(model_card_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiModelCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_model_card(
        self,
        model_card_id: str,
        request: main_models.GetAiModelCardRequest,
    ) -> main_models.GetAiModelCardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_ai_model_card_with_options(model_card_id, request, headers, runtime)

    async def get_ai_model_card_async(
        self,
        model_card_id: str,
        request: main_models.GetAiModelCardRequest,
    ) -> main_models.GetAiModelCardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_ai_model_card_with_options_async(model_card_id, request, headers, runtime)

    def get_ai_model_provider_with_options(
        self,
        model_provider_id: str,
        request: main_models.GetAiModelProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAiModelProviderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAiModelProvider',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-providers/{DaraURL.percent_encode(model_provider_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiModelProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ai_model_provider_with_options_async(
        self,
        model_provider_id: str,
        request: main_models.GetAiModelProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAiModelProviderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAiModelProvider',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-providers/{DaraURL.percent_encode(model_provider_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAiModelProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ai_model_provider(
        self,
        model_provider_id: str,
        request: main_models.GetAiModelProviderRequest,
    ) -> main_models.GetAiModelProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_ai_model_provider_with_options(model_provider_id, request, headers, runtime)

    async def get_ai_model_provider_async(
        self,
        model_provider_id: str,
        request: main_models.GetAiModelProviderRequest,
    ) -> main_models.GetAiModelProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_ai_model_provider_with_options_async(model_provider_id, request, headers, runtime)

    def get_batch_export_task_with_options(
        self,
        task_id: str,
        request: main_models.GetBatchExportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchExportTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBatchExportTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-api-batch-export-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_export_task_with_options_async(
        self,
        task_id: str,
        request: main_models.GetBatchExportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchExportTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBatchExportTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-api-batch-export-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_export_task(
        self,
        task_id: str,
        request: main_models.GetBatchExportTaskRequest,
    ) -> main_models.GetBatchExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_batch_export_task_with_options(task_id, request, headers, runtime)

    async def get_batch_export_task_async(
        self,
        task_id: str,
        request: main_models.GetBatchExportTaskRequest,
    ) -> main_models.GetBatchExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_batch_export_task_with_options_async(task_id, request, headers, runtime)

    def get_batch_import_task_with_options(
        self,
        task_id: str,
        request: main_models.GetBatchImportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchImportTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBatchImportTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-api-batch-import-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_import_task_with_options_async(
        self,
        task_id: str,
        request: main_models.GetBatchImportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchImportTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBatchImportTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-api-batch-import-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_import_task(
        self,
        task_id: str,
        request: main_models.GetBatchImportTaskRequest,
    ) -> main_models.GetBatchImportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_batch_import_task_with_options(task_id, request, headers, runtime)

    async def get_batch_import_task_async(
        self,
        task_id: str,
        request: main_models.GetBatchImportTaskRequest,
    ) -> main_models.GetBatchImportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_batch_import_task_with_options_async(task_id, request, headers, runtime)

    def get_consumer_with_options(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_with_options_async(
        self,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer(
        self,
        consumer_id: str,
    ) -> main_models.GetConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consumer_with_options(consumer_id, headers, runtime)

    async def get_consumer_async(
        self,
        consumer_id: str,
    ) -> main_models.GetConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consumer_with_options_async(consumer_id, headers, runtime)

    def get_consumer_authorization_rule_with_options(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_authorization_rule_with_options_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_authorization_rule(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> main_models.GetConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consumer_authorization_rule_with_options(consumer_authorization_rule_id, consumer_id, headers, runtime)

    async def get_consumer_authorization_rule_async(
        self,
        consumer_authorization_rule_id: str,
        consumer_id: str,
    ) -> main_models.GetConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consumer_authorization_rule_with_options_async(consumer_authorization_rule_id, consumer_id, headers, runtime)

    def get_consumer_group_with_options(
        self,
        consumer_group_id: str,
        request: main_models.GetConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_group_with_options_async(
        self,
        consumer_group_id: str,
        request: main_models.GetConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_group(
        self,
        consumer_group_id: str,
        request: main_models.GetConsumerGroupRequest,
    ) -> main_models.GetConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consumer_group_with_options(consumer_group_id, request, headers, runtime)

    async def get_consumer_group_async(
        self,
        consumer_group_id: str,
        request: main_models.GetConsumerGroupRequest,
    ) -> main_models.GetConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consumer_group_with_options_async(consumer_group_id, request, headers, runtime)

    def get_dashboard_with_options(
        self,
        gateway_id: str,
        tmp_req: main_models.GetDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDashboardResponse:
        tmp_req.validate()
        request = main_models.GetDashboardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.api_id):
            query['apiId'] = request.api_id
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.route_id):
            query['routeId'] = request.route_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.upstream_cluster):
            query['upstreamCluster'] = request.upstream_cluster
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDashboard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/dashboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDashboardResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dashboard_with_options_async(
        self,
        gateway_id: str,
        tmp_req: main_models.GetDashboardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDashboardResponse:
        tmp_req.validate()
        request = main_models.GetDashboardShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.api_id):
            query['apiId'] = request.api_id
        if not DaraCore.is_null(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.route_id):
            query['routeId'] = request.route_id
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.upstream_cluster):
            query['upstreamCluster'] = request.upstream_cluster
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDashboard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/dashboards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDashboardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dashboard(
        self,
        gateway_id: str,
        request: main_models.GetDashboardRequest,
    ) -> main_models.GetDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dashboard_with_options(gateway_id, request, headers, runtime)

    async def get_dashboard_async(
        self,
        gateway_id: str,
        request: main_models.GetDashboardRequest,
    ) -> main_models.GetDashboardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dashboard_with_options_async(gateway_id, request, headers, runtime)

    def get_domain_with_options(
        self,
        domain_id: str,
        request: main_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_with_options_async(
        self,
        domain_id: str,
        request: main_models.GetDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain(
        self,
        domain_id: str,
        request: main_models.GetDomainRequest,
    ) -> main_models.GetDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_domain_with_options(domain_id, request, headers, runtime)

    async def get_domain_async(
        self,
        domain_id: str,
        request: main_models.GetDomainRequest,
    ) -> main_models.GetDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_domain_with_options_async(domain_id, request, headers, runtime)

    def get_environment_with_options(
        self,
        environment_id: str,
        request: main_models.GetEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        if not DaraCore.is_null(request.with_vpc_info):
            query['withVpcInfo'] = request.with_vpc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_environment_with_options_async(
        self,
        environment_id: str,
        request: main_models.GetEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.with_statistics):
            query['withStatistics'] = request.with_statistics
        if not DaraCore.is_null(request.with_vpc_info):
            query['withVpcInfo'] = request.with_vpc_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_environment(
        self,
        environment_id: str,
        request: main_models.GetEnvironmentRequest,
    ) -> main_models.GetEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_environment_with_options(environment_id, request, headers, runtime)

    async def get_environment_async(
        self,
        environment_id: str,
        request: main_models.GetEnvironmentRequest,
    ) -> main_models.GetEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_environment_with_options_async(environment_id, request, headers, runtime)

    def get_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway(
        self,
        gateway_id: str,
    ) -> main_models.GetGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gateway_with_options(gateway_id, headers, runtime)

    async def get_gateway_async(
        self,
        gateway_id: str,
    ) -> main_models.GetGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gateway_with_options_async(gateway_id, headers, runtime)

    def get_gateway_elastic_policy_with_options(
        self,
        gateway_id: str,
        request: main_models.GetGatewayElasticPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayElasticPolicyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayElasticPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/elastic-policy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayElasticPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_elastic_policy_with_options_async(
        self,
        gateway_id: str,
        request: main_models.GetGatewayElasticPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayElasticPolicyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayElasticPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/elastic-policy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayElasticPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_elastic_policy(
        self,
        gateway_id: str,
        request: main_models.GetGatewayElasticPolicyRequest,
    ) -> main_models.GetGatewayElasticPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gateway_elastic_policy_with_options(gateway_id, request, headers, runtime)

    async def get_gateway_elastic_policy_async(
        self,
        gateway_id: str,
        request: main_models.GetGatewayElasticPolicyRequest,
    ) -> main_models.GetGatewayElasticPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gateway_elastic_policy_with_options_async(gateway_id, request, headers, runtime)

    def get_gateway_quota_rule_with_options(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.GetGatewayQuotaRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayQuotaRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_page_number):
            query['consumerPageNumber'] = request.consumer_page_number
        if not DaraCore.is_null(request.consumer_page_size):
            query['consumerPageSize'] = request.consumer_page_size
        if not DaraCore.is_null(request.with_consumers):
            query['withConsumers'] = request.with_consumers
        if not DaraCore.is_null(request.with_subjects):
            query['withSubjects'] = request.with_subjects
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayQuotaRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayQuotaRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_quota_rule_with_options_async(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.GetGatewayQuotaRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayQuotaRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_page_number):
            query['consumerPageNumber'] = request.consumer_page_number
        if not DaraCore.is_null(request.consumer_page_size):
            query['consumerPageSize'] = request.consumer_page_size
        if not DaraCore.is_null(request.with_consumers):
            query['withConsumers'] = request.with_consumers
        if not DaraCore.is_null(request.with_subjects):
            query['withSubjects'] = request.with_subjects
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayQuotaRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayQuotaRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_quota_rule(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.GetGatewayQuotaRuleRequest,
    ) -> main_models.GetGatewayQuotaRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gateway_quota_rule_with_options(gateway_id, rule_id, request, headers, runtime)

    async def get_gateway_quota_rule_async(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.GetGatewayQuotaRuleRequest,
    ) -> main_models.GetGatewayQuotaRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gateway_quota_rule_with_options_async(gateway_id, rule_id, request, headers, runtime)

    def get_gateway_quota_rule_subject_usage_with_options(
        self,
        gateway_id: str,
        rule_id: str,
        subject_id: str,
        request: main_models.GetGatewayQuotaRuleSubjectUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayQuotaRuleSubjectUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_failed_requests):
            query['filterFailedRequests'] = request.filter_failed_requests
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayQuotaRuleSubjectUsage',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}/subjects/{DaraURL.percent_encode(subject_id)}/usage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayQuotaRuleSubjectUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_quota_rule_subject_usage_with_options_async(
        self,
        gateway_id: str,
        rule_id: str,
        subject_id: str,
        request: main_models.GetGatewayQuotaRuleSubjectUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGatewayQuotaRuleSubjectUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_failed_requests):
            query['filterFailedRequests'] = request.filter_failed_requests
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGatewayQuotaRuleSubjectUsage',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}/subjects/{DaraURL.percent_encode(subject_id)}/usage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGatewayQuotaRuleSubjectUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_quota_rule_subject_usage(
        self,
        gateway_id: str,
        rule_id: str,
        subject_id: str,
        request: main_models.GetGatewayQuotaRuleSubjectUsageRequest,
    ) -> main_models.GetGatewayQuotaRuleSubjectUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_gateway_quota_rule_subject_usage_with_options(gateway_id, rule_id, subject_id, request, headers, runtime)

    async def get_gateway_quota_rule_subject_usage_async(
        self,
        gateway_id: str,
        rule_id: str,
        subject_id: str,
        request: main_models.GetGatewayQuotaRuleSubjectUsageRequest,
    ) -> main_models.GetGatewayQuotaRuleSubjectUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_gateway_quota_rule_subject_usage_with_options_async(gateway_id, rule_id, subject_id, request, headers, runtime)

    def get_http_api_with_options(
        self,
        http_api_id: str,
        request: main_models.GetHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expand_policy_configs):
            query['expandPolicyConfigs'] = request.expand_policy_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_with_options_async(
        self,
        http_api_id: str,
        request: main_models.GetHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expand_policy_configs):
            query['expandPolicyConfigs'] = request.expand_policy_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api(
        self,
        http_api_id: str,
        request: main_models.GetHttpApiRequest,
    ) -> main_models.GetHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_http_api_with_options(http_api_id, request, headers, runtime)

    async def get_http_api_async(
        self,
        http_api_id: str,
        request: main_models.GetHttpApiRequest,
    ) -> main_models.GetHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_http_api_with_options_async(http_api_id, request, headers, runtime)

    def get_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiOperationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiOperationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> main_models.GetHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_http_api_operation_with_options(http_api_id, operation_id, headers, runtime)

    async def get_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
    ) -> main_models.GetHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_http_api_operation_with_options_async(http_api_id, operation_id, headers, runtime)

    def get_http_api_route_with_options(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiRouteResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_http_api_route_with_options_async(
        self,
        http_api_id: str,
        route_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHttpApiRouteResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_http_api_route(
        self,
        http_api_id: str,
        route_id: str,
    ) -> main_models.GetHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_http_api_route_with_options(http_api_id, route_id, headers, runtime)

    async def get_http_api_route_async(
        self,
        http_api_id: str,
        route_id: str,
    ) -> main_models.GetHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_http_api_route_with_options_async(http_api_id, route_id, headers, runtime)

    def get_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mcp_server(
        self,
        mcp_server_id: str,
    ) -> main_models.GetMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def get_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> main_models.GetMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def get_migration_namespaced_services_with_options(
        self,
        task_id: str,
        request: main_models.GetMigrationNamespacedServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMigrationNamespacedServicesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMigrationNamespacedServices',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks/{DaraURL.percent_encode(task_id)}/namespaced-services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMigrationNamespacedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_migration_namespaced_services_with_options_async(
        self,
        task_id: str,
        request: main_models.GetMigrationNamespacedServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMigrationNamespacedServicesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMigrationNamespacedServices',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks/{DaraURL.percent_encode(task_id)}/namespaced-services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMigrationNamespacedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_migration_namespaced_services(
        self,
        task_id: str,
        request: main_models.GetMigrationNamespacedServicesRequest,
    ) -> main_models.GetMigrationNamespacedServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_migration_namespaced_services_with_options(task_id, request, headers, runtime)

    async def get_migration_namespaced_services_async(
        self,
        task_id: str,
        request: main_models.GetMigrationNamespacedServicesRequest,
    ) -> main_models.GetMigrationNamespacedServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_migration_namespaced_services_with_options_async(task_id, request, headers, runtime)

    def get_migration_task_with_options(
        self,
        task_id: str,
        request: main_models.GetMigrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMigrationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMigrationTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_migration_task_with_options_async(
        self,
        task_id: str,
        request: main_models.GetMigrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMigrationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMigrationTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMigrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_migration_task(
        self,
        task_id: str,
        request: main_models.GetMigrationTaskRequest,
    ) -> main_models.GetMigrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_migration_task_with_options(task_id, request, headers, runtime)

    async def get_migration_task_async(
        self,
        task_id: str,
        request: main_models.GetMigrationTaskRequest,
    ) -> main_models.GetMigrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_migration_task_with_options_async(task_id, request, headers, runtime)

    def get_plugin_attachment_with_options(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_plugin_attachment_with_options_async(
        self,
        plugin_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_plugin_attachment(
        self,
        plugin_attachment_id: str,
    ) -> main_models.GetPluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_plugin_attachment_with_options(plugin_attachment_id, headers, runtime)

    async def get_plugin_attachment_async(
        self,
        plugin_attachment_id: str,
    ) -> main_models.GetPluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_plugin_attachment_with_options_async(plugin_attachment_id, headers, runtime)

    def get_plugin_class_with_options(
        self,
        plugin_class_id: str,
        request: main_models.GetPluginClassRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginClassResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPluginClass',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-classes/{DaraURL.percent_encode(plugin_class_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_plugin_class_with_options_async(
        self,
        plugin_class_id: str,
        request: main_models.GetPluginClassRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginClassResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPluginClass',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-classes/{DaraURL.percent_encode(plugin_class_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_plugin_class(
        self,
        plugin_class_id: str,
        request: main_models.GetPluginClassRequest,
    ) -> main_models.GetPluginClassResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_plugin_class_with_options(plugin_class_id, request, headers, runtime)

    async def get_plugin_class_async(
        self,
        plugin_class_id: str,
        request: main_models.GetPluginClassRequest,
    ) -> main_models.GetPluginClassResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_plugin_class_with_options_async(plugin_class_id, request, headers, runtime)

    def get_plugin_workspace_with_options(
        self,
        workspace_id: str,
        request: main_models.GetPluginWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPluginWorkspace',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_plugin_workspace_with_options_async(
        self,
        workspace_id: str,
        request: main_models.GetPluginWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPluginWorkspaceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPluginWorkspace',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-workspaces/{DaraURL.percent_encode(workspace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPluginWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_plugin_workspace(
        self,
        workspace_id: str,
        request: main_models.GetPluginWorkspaceRequest,
    ) -> main_models.GetPluginWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_plugin_workspace_with_options(workspace_id, request, headers, runtime)

    async def get_plugin_workspace_async(
        self,
        workspace_id: str,
        request: main_models.GetPluginWorkspaceRequest,
    ) -> main_models.GetPluginWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_plugin_workspace_with_options_async(workspace_id, request, headers, runtime)

    def get_policy_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        policy_id: str,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_policy_with_options(policy_id, headers, runtime)

    async def get_policy_async(
        self,
        policy_id: str,
    ) -> main_models.GetPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_policy_with_options_async(policy_id, headers, runtime)

    def get_policy_attachment_with_options(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments/{DaraURL.percent_encode(policy_attachment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_attachment_with_options_async(
        self,
        policy_attachment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPolicyAttachmentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPolicyAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-attachments/{DaraURL.percent_encode(policy_attachment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPolicyAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_attachment(
        self,
        policy_attachment_id: str,
    ) -> main_models.GetPolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_policy_attachment_with_options(policy_attachment_id, headers, runtime)

    async def get_policy_attachment_async(
        self,
        policy_attachment_id: str,
    ) -> main_models.GetPolicyAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_policy_attachment_with_options_async(policy_attachment_id, headers, runtime)

    def get_resource_overview_with_options(
        self,
        request: main_models.GetResourceOverviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceOverview',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/overview/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_overview_with_options_async(
        self,
        request: main_models.GetResourceOverviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceOverview',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/overview/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_overview(
        self,
        request: main_models.GetResourceOverviewRequest,
    ) -> main_models.GetResourceOverviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_overview_with_options(request, headers, runtime)

    async def get_resource_overview_async(
        self,
        request: main_models.GetResourceOverviewRequest,
    ) -> main_models.GetResourceOverviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_overview_with_options_async(request, headers, runtime)

    def get_risk_notification_with_options(
        self,
        gateway_id: str,
        request: main_models.GetRiskNotificationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRiskNotificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.risk_code):
            query['riskCode'] = request.risk_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRiskNotification',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/risk-check/notifications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRiskNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_notification_with_options_async(
        self,
        gateway_id: str,
        request: main_models.GetRiskNotificationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRiskNotificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.risk_code):
            query['riskCode'] = request.risk_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRiskNotification',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/risk-check/notifications',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRiskNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_notification(
        self,
        gateway_id: str,
        request: main_models.GetRiskNotificationRequest,
    ) -> main_models.GetRiskNotificationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_risk_notification_with_options(gateway_id, request, headers, runtime)

    async def get_risk_notification_async(
        self,
        gateway_id: str,
        request: main_models.GetRiskNotificationRequest,
    ) -> main_models.GetRiskNotificationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_risk_notification_with_options_async(gateway_id, request, headers, runtime)

    def get_secret_with_options(
        self,
        secret_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSecret',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets/{DaraURL.percent_encode(secret_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_with_options_async(
        self,
        secret_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSecret',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets/{DaraURL.percent_encode(secret_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret(
        self,
        secret_id: str,
    ) -> main_models.GetSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_secret_with_options(secret_id, headers, runtime)

    async def get_secret_async(
        self,
        secret_id: str,
    ) -> main_models.GetSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_secret_with_options_async(secret_id, headers, runtime)

    def get_secret_value_with_options(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretValueResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSecretValue',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets/name/{DaraURL.percent_encode(name)}/value',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretValueResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_value_with_options_async(
        self,
        name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretValueResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSecretValue',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets/name/{DaraURL.percent_encode(name)}/value',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretValueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_value(
        self,
        name: str,
    ) -> main_models.GetSecretValueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_secret_value_with_options(name, headers, runtime)

    async def get_secret_value_async(
        self,
        name: str,
    ) -> main_models.GetSecretValueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_secret_value_with_options_async(name, headers, runtime)

    def get_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        service_id: str,
    ) -> main_models.GetServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_service_with_options(service_id, headers, runtime)

    async def get_service_async(
        self,
        service_id: str,
    ) -> main_models.GetServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_service_with_options_async(service_id, headers, runtime)

    def get_source_with_options(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources/{DaraURL.percent_encode(source_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_source_with_options_async(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetSource',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources/{DaraURL.percent_encode(source_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_source(
        self,
        source_id: str,
    ) -> main_models.GetSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_source_with_options(source_id, headers, runtime)

    async def get_source_async(
        self,
        source_id: str,
    ) -> main_models.GetSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_source_with_options_async(source_id, headers, runtime)

    def get_trace_config_with_options(
        self,
        gateway_id: str,
        request: main_models.GetTraceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceConfig',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/trace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_config_with_options_async(
        self,
        gateway_id: str,
        request: main_models.GetTraceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceConfig',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/trace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace_config(
        self,
        gateway_id: str,
        request: main_models.GetTraceConfigRequest,
    ) -> main_models.GetTraceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_trace_config_with_options(gateway_id, request, headers, runtime)

    async def get_trace_config_async(
        self,
        gateway_id: str,
        request: main_models.GetTraceConfigRequest,
    ) -> main_models.GetTraceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_trace_config_with_options_async(gateway_id, request, headers, runtime)

    def import_http_api_with_options(
        self,
        request: main_models.ImportHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ImportHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.mcp_route_id):
            body['mcpRouteId'] = request.mcp_route_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec_content_base_64):
            body['specContentBase64'] = request.spec_content_base_64
        if not DaraCore.is_null(request.spec_file_url):
            body['specFileUrl'] = request.spec_file_url
        if not DaraCore.is_null(request.spec_oss_config):
            body['specOssConfig'] = request.spec_oss_config
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        if not DaraCore.is_null(request.target_http_api_id):
            body['targetHttpApiId'] = request.target_http_api_id
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        if not DaraCore.is_null(request.with_gateway_extension):
            body['withGatewayExtension'] = request.with_gateway_extension
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/import',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_http_api_with_options_async(
        self,
        request: main_models.ImportHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ImportHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.mcp_route_id):
            body['mcpRouteId'] = request.mcp_route_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.spec_content_base_64):
            body['specContentBase64'] = request.spec_content_base_64
        if not DaraCore.is_null(request.spec_file_url):
            body['specFileUrl'] = request.spec_file_url
        if not DaraCore.is_null(request.spec_oss_config):
            body['specOssConfig'] = request.spec_oss_config
        if not DaraCore.is_null(request.strategy):
            body['strategy'] = request.strategy
        if not DaraCore.is_null(request.target_http_api_id):
            body['targetHttpApiId'] = request.target_http_api_id
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        if not DaraCore.is_null(request.with_gateway_extension):
            body['withGatewayExtension'] = request.with_gateway_extension
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/import',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_http_api(
        self,
        request: main_models.ImportHttpApiRequest,
    ) -> main_models.ImportHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.import_http_api_with_options(request, headers, runtime)

    async def import_http_api_async(
        self,
        request: main_models.ImportHttpApiRequest,
    ) -> main_models.ImportHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.import_http_api_with_options_async(request, headers, runtime)

    def install_plugin_with_options(
        self,
        request: main_models.InstallPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallPluginResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_ids):
            body['gatewayIds'] = request.gateway_ids
        if not DaraCore.is_null(request.plugin_class_id):
            body['pluginClassId'] = request.plugin_class_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallPlugin',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_plugin_with_options_async(
        self,
        request: main_models.InstallPluginRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InstallPluginResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.gateway_ids):
            body['gatewayIds'] = request.gateway_ids
        if not DaraCore.is_null(request.plugin_class_id):
            body['pluginClassId'] = request.plugin_class_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InstallPlugin',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins/',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_plugin(
        self,
        request: main_models.InstallPluginRequest,
    ) -> main_models.InstallPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.install_plugin_with_options(request, headers, runtime)

    async def install_plugin_async(
        self,
        request: main_models.InstallPluginRequest,
    ) -> main_models.InstallPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.install_plugin_with_options_async(request, headers, runtime)

    def invoke_aiagent_with_sse(
        self,
        request: main_models.InvokeAIAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.InvokeAIAgentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.biz_params):
            body['bizParams'] = request.biz_params
        if not DaraCore.is_null(request.history):
            body['history'] = request.history
        if not DaraCore.is_null(request.output_language):
            body['outputLanguage'] = request.output_language
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAIAgent',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-agents/invoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.InvokeAIAgentResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def invoke_aiagent_with_sse_async(
        self,
        request: main_models.InvokeAIAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.InvokeAIAgentResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.biz_params):
            body['bizParams'] = request.biz_params
        if not DaraCore.is_null(request.history):
            body['history'] = request.history
        if not DaraCore.is_null(request.output_language):
            body['outputLanguage'] = request.output_language
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAIAgent',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-agents/invoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.InvokeAIAgentResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def invoke_aiagent_with_options(
        self,
        request: main_models.InvokeAIAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvokeAIAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.biz_params):
            body['bizParams'] = request.biz_params
        if not DaraCore.is_null(request.history):
            body['history'] = request.history
        if not DaraCore.is_null(request.output_language):
            body['outputLanguage'] = request.output_language
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAIAgent',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-agents/invoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeAIAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_aiagent_with_options_async(
        self,
        request: main_models.InvokeAIAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvokeAIAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.biz_params):
            body['bizParams'] = request.biz_params
        if not DaraCore.is_null(request.history):
            body['history'] = request.history
        if not DaraCore.is_null(request.output_language):
            body['outputLanguage'] = request.output_language
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InvokeAIAgent',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-agents/invoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeAIAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_aiagent(
        self,
        request: main_models.InvokeAIAgentRequest,
    ) -> main_models.InvokeAIAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.invoke_aiagent_with_options(request, headers, runtime)

    async def invoke_aiagent_async(
        self,
        request: main_models.InvokeAIAgentRequest,
    ) -> main_models.InvokeAIAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.invoke_aiagent_with_options_async(request, headers, runtime)

    def list_ai_model_cards_with_options(
        self,
        request: main_models.ListAiModelCardsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAiModelCardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAiModelCards',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-cards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAiModelCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ai_model_cards_with_options_async(
        self,
        request: main_models.ListAiModelCardsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAiModelCardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAiModelCards',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-cards',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAiModelCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ai_model_cards(
        self,
        request: main_models.ListAiModelCardsRequest,
    ) -> main_models.ListAiModelCardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ai_model_cards_with_options(request, headers, runtime)

    async def list_ai_model_cards_async(
        self,
        request: main_models.ListAiModelCardsRequest,
    ) -> main_models.ListAiModelCardsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ai_model_cards_with_options_async(request, headers, runtime)

    def list_ai_model_providers_with_options(
        self,
        request: main_models.ListAiModelProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAiModelProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAiModelProviders',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAiModelProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ai_model_providers_with_options_async(
        self,
        request: main_models.ListAiModelProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAiModelProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAiModelProviders',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAiModelProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ai_model_providers(
        self,
        request: main_models.ListAiModelProvidersRequest,
    ) -> main_models.ListAiModelProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ai_model_providers_with_options(request, headers, runtime)

    async def list_ai_model_providers_async(
        self,
        request: main_models.ListAiModelProvidersRequest,
    ) -> main_models.ListAiModelProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ai_model_providers_with_options_async(request, headers, runtime)

    def list_batch_export_tasks_with_options(
        self,
        request: main_models.ListBatchExportTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBatchExportTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.statuses):
            query['statuses'] = request.statuses
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBatchExportTasks',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-api-batch-export-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBatchExportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_batch_export_tasks_with_options_async(
        self,
        request: main_models.ListBatchExportTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBatchExportTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.statuses):
            query['statuses'] = request.statuses
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBatchExportTasks',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-api-batch-export-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBatchExportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_batch_export_tasks(
        self,
        request: main_models.ListBatchExportTasksRequest,
    ) -> main_models.ListBatchExportTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_batch_export_tasks_with_options(request, headers, runtime)

    async def list_batch_export_tasks_async(
        self,
        request: main_models.ListBatchExportTasksRequest,
    ) -> main_models.ListBatchExportTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_batch_export_tasks_with_options_async(request, headers, runtime)

    def list_consumer_authorization_rules_with_options(
        self,
        consumer_id: str,
        request: main_models.ListConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerAuthorizationRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name_like):
            query['apiNameLike'] = request.api_name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerAuthorizationRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumer_authorization_rules_with_options_async(
        self,
        consumer_id: str,
        request: main_models.ListConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerAuthorizationRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name_like):
            query['apiNameLike'] = request.api_name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerAuthorizationRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerAuthorizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumer_authorization_rules(
        self,
        consumer_id: str,
        request: main_models.ListConsumerAuthorizationRulesRequest,
    ) -> main_models.ListConsumerAuthorizationRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumer_authorization_rules_with_options(consumer_id, request, headers, runtime)

    async def list_consumer_authorization_rules_async(
        self,
        consumer_id: str,
        request: main_models.ListConsumerAuthorizationRulesRequest,
    ) -> main_models.ListConsumerAuthorizationRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumer_authorization_rules_with_options_async(consumer_id, request, headers, runtime)

    def list_consumer_group_consumers_with_options(
        self,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupConsumersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupConsumersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerGroupConsumers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}/consumers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerGroupConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumer_group_consumers_with_options_async(
        self,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupConsumersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupConsumersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerGroupConsumers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}/consumers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerGroupConsumersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumer_group_consumers(
        self,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupConsumersRequest,
    ) -> main_models.ListConsumerGroupConsumersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumer_group_consumers_with_options(consumer_group_id, request, headers, runtime)

    async def list_consumer_group_consumers_async(
        self,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupConsumersRequest,
    ) -> main_models.ListConsumerGroupConsumersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumer_group_consumers_with_options_async(consumer_group_id, request, headers, runtime)

    def list_consumer_group_quota_rules_with_options(
        self,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupQuotaRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupQuotaRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerGroupQuotaRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}/quota-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerGroupQuotaRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumer_group_quota_rules_with_options_async(
        self,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupQuotaRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupQuotaRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerGroupQuotaRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}/quota-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerGroupQuotaRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumer_group_quota_rules(
        self,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupQuotaRulesRequest,
    ) -> main_models.ListConsumerGroupQuotaRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumer_group_quota_rules_with_options(consumer_group_id, request, headers, runtime)

    async def list_consumer_group_quota_rules_async(
        self,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupQuotaRulesRequest,
    ) -> main_models.ListConsumerGroupQuotaRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumer_group_quota_rules_with_options_async(consumer_group_id, request, headers, runtime)

    def list_consumer_groups_with_options(
        self,
        request: main_models.ListConsumerGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerGroups',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumer_groups_with_options_async(
        self,
        request: main_models.ListConsumerGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerGroups',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumer_groups(
        self,
        request: main_models.ListConsumerGroupsRequest,
    ) -> main_models.ListConsumerGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumer_groups_with_options(request, headers, runtime)

    async def list_consumer_groups_async(
        self,
        request: main_models.ListConsumerGroupsRequest,
    ) -> main_models.ListConsumerGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumer_groups_with_options_async(request, headers, runtime)

    def list_consumer_quota_rules_with_options(
        self,
        consumer_id: str,
        request: main_models.ListConsumerQuotaRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerQuotaRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerQuotaRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/quota-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerQuotaRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumer_quota_rules_with_options_async(
        self,
        consumer_id: str,
        request: main_models.ListConsumerQuotaRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerQuotaRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerQuotaRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/quota-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerQuotaRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumer_quota_rules(
        self,
        consumer_id: str,
        request: main_models.ListConsumerQuotaRulesRequest,
    ) -> main_models.ListConsumerQuotaRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumer_quota_rules_with_options(consumer_id, request, headers, runtime)

    async def list_consumer_quota_rules_async(
        self,
        consumer_id: str,
        request: main_models.ListConsumerQuotaRulesRequest,
    ) -> main_models.ListConsumerQuotaRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumer_quota_rules_with_options_async(consumer_id, request, headers, runtime)

    def list_consumers_with_options(
        self,
        request: main_models.ListConsumersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumers_with_options_async(
        self,
        request: main_models.ListConsumersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumers(
        self,
        request: main_models.ListConsumersRequest,
    ) -> main_models.ListConsumersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumers_with_options(request, headers, runtime)

    async def list_consumers_async(
        self,
        request: main_models.ListConsumersRequest,
    ) -> main_models.ListConsumersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumers_with_options_async(request, headers, runtime)

    def list_domains_with_options(
        self,
        request: main_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_scope):
            query['domainScope'] = request.domain_scope
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_domains_with_options_async(
        self,
        request: main_models.ListDomainsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_scope):
            query['domainScope'] = request.domain_scope
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDomains',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_domains(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_domains_with_options(request, headers, runtime)

    async def list_domains_async(
        self,
        request: main_models.ListDomainsRequest,
    ) -> main_models.ListDomainsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_domains_with_options_async(request, headers, runtime)

    def list_environments_with_options(
        self,
        request: main_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_like):
            query['aliasLike'] = request.alias_like
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_name_like):
            query['gatewayNameLike'] = request.gateway_name_like
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironments',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        request: main_models.ListEnvironmentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_like):
            query['aliasLike'] = request.alias_like
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_name_like):
            query['gatewayNameLike'] = request.gateway_name_like
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironments',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(
        self,
        request: main_models.ListEnvironmentsRequest,
    ) -> main_models.ListEnvironmentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_environments_with_options(request, headers, runtime)

    async def list_environments_async(
        self,
        request: main_models.ListEnvironmentsRequest,
    ) -> main_models.ListEnvironmentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_environments_with_options_async(request, headers, runtime)

    def list_external_services_with_options(
        self,
        gateway_id: str,
        request: main_models.ListExternalServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.importable_only):
            query['importableOnly'] = request.importable_only
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.pai_workspace_id):
            query['paiWorkspaceId'] = request.pai_workspace_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExternalServices',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/external-services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_external_services_with_options_async(
        self,
        gateway_id: str,
        request: main_models.ListExternalServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExternalServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.importable_only):
            query['importableOnly'] = request.importable_only
        if not DaraCore.is_null(request.limit):
            query['limit'] = request.limit
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.pai_workspace_id):
            query['paiWorkspaceId'] = request.pai_workspace_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExternalServices',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/external-services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExternalServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_external_services(
        self,
        gateway_id: str,
        request: main_models.ListExternalServicesRequest,
    ) -> main_models.ListExternalServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_external_services_with_options(gateway_id, request, headers, runtime)

    async def list_external_services_async(
        self,
        gateway_id: str,
        request: main_models.ListExternalServicesRequest,
    ) -> main_models.ListExternalServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_external_services_with_options_async(gateway_id, request, headers, runtime)

    def list_gateway_authorizable_security_groups_with_options(
        self,
        gateway_id: str,
        request: main_models.ListGatewayAuthorizableSecurityGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayAuthorizableSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cs_cluster_id):
            query['csClusterId'] = request.cs_cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayAuthorizableSecurityGroups',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/authorizable-security-groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayAuthorizableSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_authorizable_security_groups_with_options_async(
        self,
        gateway_id: str,
        request: main_models.ListGatewayAuthorizableSecurityGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayAuthorizableSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cs_cluster_id):
            query['csClusterId'] = request.cs_cluster_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayAuthorizableSecurityGroups',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/authorizable-security-groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayAuthorizableSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_authorizable_security_groups(
        self,
        gateway_id: str,
        request: main_models.ListGatewayAuthorizableSecurityGroupsRequest,
    ) -> main_models.ListGatewayAuthorizableSecurityGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_authorizable_security_groups_with_options(gateway_id, request, headers, runtime)

    async def list_gateway_authorizable_security_groups_async(
        self,
        gateway_id: str,
        request: main_models.ListGatewayAuthorizableSecurityGroupsRequest,
    ) -> main_models.ListGatewayAuthorizableSecurityGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_authorizable_security_groups_with_options_async(gateway_id, request, headers, runtime)

    def list_gateway_authorized_security_group_rules_with_options(
        self,
        gateway_id: str,
        request: main_models.ListGatewayAuthorizedSecurityGroupRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayAuthorizedSecurityGroupRulesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayAuthorizedSecurityGroupRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/authorized-security-groups-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayAuthorizedSecurityGroupRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_authorized_security_group_rules_with_options_async(
        self,
        gateway_id: str,
        request: main_models.ListGatewayAuthorizedSecurityGroupRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayAuthorizedSecurityGroupRulesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayAuthorizedSecurityGroupRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/authorized-security-groups-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayAuthorizedSecurityGroupRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_authorized_security_group_rules(
        self,
        gateway_id: str,
        request: main_models.ListGatewayAuthorizedSecurityGroupRulesRequest,
    ) -> main_models.ListGatewayAuthorizedSecurityGroupRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_authorized_security_group_rules_with_options(gateway_id, request, headers, runtime)

    async def list_gateway_authorized_security_group_rules_async(
        self,
        gateway_id: str,
        request: main_models.ListGatewayAuthorizedSecurityGroupRulesRequest,
    ) -> main_models.ListGatewayAuthorizedSecurityGroupRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_authorized_security_group_rules_with_options_async(gateway_id, request, headers, runtime)

    def list_gateway_error_access_logs_with_options(
        self,
        gateway_id: str,
        request: main_models.ListGatewayErrorAccessLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayErrorAccessLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authority):
            query['authority'] = request.authority
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.gateway_request_id):
            query['gatewayRequestId'] = request.gateway_request_id
        if not DaraCore.is_null(request.path):
            query['path'] = request.path
        if not DaraCore.is_null(request.response_code):
            query['responseCode'] = request.response_code
        if not DaraCore.is_null(request.route_name):
            query['routeName'] = request.route_name
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayErrorAccessLogs',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/error-access-logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayErrorAccessLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_error_access_logs_with_options_async(
        self,
        gateway_id: str,
        request: main_models.ListGatewayErrorAccessLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayErrorAccessLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authority):
            query['authority'] = request.authority
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.gateway_request_id):
            query['gatewayRequestId'] = request.gateway_request_id
        if not DaraCore.is_null(request.path):
            query['path'] = request.path
        if not DaraCore.is_null(request.response_code):
            query['responseCode'] = request.response_code
        if not DaraCore.is_null(request.route_name):
            query['routeName'] = request.route_name
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayErrorAccessLogs',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/error-access-logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayErrorAccessLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_error_access_logs(
        self,
        gateway_id: str,
        request: main_models.ListGatewayErrorAccessLogsRequest,
    ) -> main_models.ListGatewayErrorAccessLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_error_access_logs_with_options(gateway_id, request, headers, runtime)

    async def list_gateway_error_access_logs_async(
        self,
        gateway_id: str,
        request: main_models.ListGatewayErrorAccessLogsRequest,
    ) -> main_models.ListGatewayErrorAccessLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_error_access_logs_with_options_async(gateway_id, request, headers, runtime)

    def list_gateway_features_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayFeaturesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayFeatures',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/gateway-features',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_features_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayFeaturesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayFeatures',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/gateway-features',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_features(
        self,
        gateway_id: str,
    ) -> main_models.ListGatewayFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_features_with_options(gateway_id, headers, runtime)

    async def list_gateway_features_async(
        self,
        gateway_id: str,
    ) -> main_models.ListGatewayFeaturesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_features_with_options_async(gateway_id, headers, runtime)

    def list_gateway_load_balancers_with_options(
        self,
        gateway_id: str,
        request: main_models.ListGatewayLoadBalancersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.load_balancer_id):
            query['loadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.network):
            query['network'] = request.network
        if not DaraCore.is_null(request.related):
            query['related'] = request.related
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayLoadBalancers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/list-load-balancers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_load_balancers_with_options_async(
        self,
        gateway_id: str,
        request: main_models.ListGatewayLoadBalancersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayLoadBalancersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.load_balancer_id):
            query['loadBalancerId'] = request.load_balancer_id
        if not DaraCore.is_null(request.network):
            query['network'] = request.network
        if not DaraCore.is_null(request.related):
            query['related'] = request.related
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayLoadBalancers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/list-load-balancers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_load_balancers(
        self,
        gateway_id: str,
        request: main_models.ListGatewayLoadBalancersRequest,
    ) -> main_models.ListGatewayLoadBalancersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_load_balancers_with_options(gateway_id, request, headers, runtime)

    async def list_gateway_load_balancers_async(
        self,
        gateway_id: str,
        request: main_models.ListGatewayLoadBalancersRequest,
    ) -> main_models.ListGatewayLoadBalancersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_load_balancers_with_options_async(gateway_id, request, headers, runtime)

    def list_gateway_quota_rules_with_options(
        self,
        gateway_id: str,
        request: main_models.ListGatewayQuotaRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayQuotaRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayQuotaRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayQuotaRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_quota_rules_with_options_async(
        self,
        gateway_id: str,
        request: main_models.ListGatewayQuotaRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewayQuotaRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGatewayQuotaRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewayQuotaRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway_quota_rules(
        self,
        gateway_id: str,
        request: main_models.ListGatewayQuotaRulesRequest,
    ) -> main_models.ListGatewayQuotaRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateway_quota_rules_with_options(gateway_id, request, headers, runtime)

    async def list_gateway_quota_rules_async(
        self,
        gateway_id: str,
        request: main_models.ListGatewayQuotaRulesRequest,
    ) -> main_models.ListGatewayQuotaRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateway_quota_rules_with_options_async(gateway_id, request, headers, runtime)

    def list_gateways_with_options(
        self,
        tmp_req: main_models.ListGatewaysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewaysResponse:
        tmp_req.validate()
        request = main_models.ListGatewaysShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGateways',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateways_with_options_async(
        self,
        tmp_req: main_models.ListGatewaysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGatewaysResponse:
        tmp_req.validate()
        request = main_models.ListGatewaysShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGateways',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateways(
        self,
        request: main_models.ListGatewaysRequest,
    ) -> main_models.ListGatewaysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_gateways_with_options(request, headers, runtime)

    async def list_gateways_async(
        self,
        request: main_models.ListGatewaysRequest,
    ) -> main_models.ListGatewaysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_gateways_with_options_async(request, headers, runtime)

    def list_global_policies_with_options(
        self,
        request: main_models.ListGlobalPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGlobalPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.class_name):
            query['className'] = request.class_name
        if not DaraCore.is_null(request.enable):
            query['enable'] = request.enable
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.global_policy_type):
            query['globalPolicyType'] = request.global_policy_type
        if not DaraCore.is_null(request.ip_access_control_content):
            query['ipAccessControlContent'] = request.ip_access_control_content
        if not DaraCore.is_null(request.ip_access_control_protocol_layer):
            query['ipAccessControlProtocolLayer'] = request.ip_access_control_protocol_layer
        if not DaraCore.is_null(request.ip_access_control_resource_name):
            query['ipAccessControlResourceName'] = request.ip_access_control_resource_name
        if not DaraCore.is_null(request.ip_access_control_type):
            query['ipAccessControlType'] = request.ip_access_control_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGlobalPolicies',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/global-policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGlobalPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_global_policies_with_options_async(
        self,
        request: main_models.ListGlobalPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGlobalPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.class_name):
            query['className'] = request.class_name
        if not DaraCore.is_null(request.enable):
            query['enable'] = request.enable
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.global_policy_type):
            query['globalPolicyType'] = request.global_policy_type
        if not DaraCore.is_null(request.ip_access_control_content):
            query['ipAccessControlContent'] = request.ip_access_control_content
        if not DaraCore.is_null(request.ip_access_control_protocol_layer):
            query['ipAccessControlProtocolLayer'] = request.ip_access_control_protocol_layer
        if not DaraCore.is_null(request.ip_access_control_resource_name):
            query['ipAccessControlResourceName'] = request.ip_access_control_resource_name
        if not DaraCore.is_null(request.ip_access_control_type):
            query['ipAccessControlType'] = request.ip_access_control_type
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGlobalPolicies',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/global-policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGlobalPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_global_policies(
        self,
        request: main_models.ListGlobalPoliciesRequest,
    ) -> main_models.ListGlobalPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_global_policies_with_options(request, headers, runtime)

    async def list_global_policies_async(
        self,
        request: main_models.ListGlobalPoliciesRequest,
    ) -> main_models.ListGlobalPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_global_policies_with_options_async(request, headers, runtime)

    def list_http_api_operations_with_options(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiOperationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApiOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not DaraCore.is_null(request.enable_auth):
            query['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.method):
            query['method'] = request.method
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.path_like):
            query['pathLike'] = request.path_like
        if not DaraCore.is_null(request.with_consumer_in_environment_id):
            query['withConsumerInEnvironmentId'] = request.with_consumer_in_environment_id
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApiOperations',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApiOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_api_operations_with_options_async(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiOperationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApiOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not DaraCore.is_null(request.enable_auth):
            query['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.method):
            query['method'] = request.method
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.path_like):
            query['pathLike'] = request.path_like
        if not DaraCore.is_null(request.with_consumer_in_environment_id):
            query['withConsumerInEnvironmentId'] = request.with_consumer_in_environment_id
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApiOperations',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApiOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_api_operations(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiOperationsRequest,
    ) -> main_models.ListHttpApiOperationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_http_api_operations_with_options(http_api_id, request, headers, runtime)

    async def list_http_api_operations_async(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiOperationsRequest,
    ) -> main_models.ListHttpApiOperationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_http_api_operations_with_options_async(http_api_id, request, headers, runtime)

    def list_http_api_routes_with_options(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiRoutesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApiRoutesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_service_name):
            query['backendServiceName'] = request.backend_service_name
        if not DaraCore.is_null(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not DaraCore.is_null(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not DaraCore.is_null(request.domain_id):
            query['domainId'] = request.domain_id
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.path_like):
            query['pathLike'] = request.path_like
        if not DaraCore.is_null(request.with_auth_policy_info):
            query['withAuthPolicyInfo'] = request.with_auth_policy_info
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApiRoutes',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApiRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_api_routes_with_options_async(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiRoutesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApiRoutesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backend_service_name):
            query['backendServiceName'] = request.backend_service_name
        if not DaraCore.is_null(request.consumer_authorization_rule_id):
            query['consumerAuthorizationRuleId'] = request.consumer_authorization_rule_id
        if not DaraCore.is_null(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not DaraCore.is_null(request.domain_id):
            query['domainId'] = request.domain_id
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.for_deploy):
            query['forDeploy'] = request.for_deploy
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.path_like):
            query['pathLike'] = request.path_like
        if not DaraCore.is_null(request.with_auth_policy_info):
            query['withAuthPolicyInfo'] = request.with_auth_policy_info
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApiRoutes',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApiRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_api_routes(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiRoutesRequest,
    ) -> main_models.ListHttpApiRoutesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_http_api_routes_with_options(http_api_id, request, headers, runtime)

    async def list_http_api_routes_async(
        self,
        http_api_id: str,
        request: main_models.ListHttpApiRoutesRequest,
    ) -> main_models.ListHttpApiRoutesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_http_api_routes_with_options_async(http_api_id, request, headers, runtime)

    def list_http_apis_with_options(
        self,
        request: main_models.ListHttpApisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.types):
            query['types'] = request.types
        if not DaraCore.is_null(request.with_apis_published_to_environment):
            query['withAPIsPublishedToEnvironment'] = request.with_apis_published_to_environment
        if not DaraCore.is_null(request.with_auth_policy_in_environment_id):
            query['withAuthPolicyInEnvironmentId'] = request.with_auth_policy_in_environment_id
        if not DaraCore.is_null(request.with_auth_policy_list):
            query['withAuthPolicyList'] = request.with_auth_policy_list
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_environment_info):
            query['withEnvironmentInfo'] = request.with_environment_info
        if not DaraCore.is_null(request.with_environment_info_by_id):
            query['withEnvironmentInfoById'] = request.with_environment_info_by_id
        if not DaraCore.is_null(request.with_ingress_info):
            query['withIngressInfo'] = request.with_ingress_info
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        if not DaraCore.is_null(request.with_policy_configs):
            query['withPolicyConfigs'] = request.with_policy_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApis',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApisResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_http_apis_with_options_async(
        self,
        request: main_models.ListHttpApisRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListHttpApisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.types):
            query['types'] = request.types
        if not DaraCore.is_null(request.with_apis_published_to_environment):
            query['withAPIsPublishedToEnvironment'] = request.with_apis_published_to_environment
        if not DaraCore.is_null(request.with_auth_policy_in_environment_id):
            query['withAuthPolicyInEnvironmentId'] = request.with_auth_policy_in_environment_id
        if not DaraCore.is_null(request.with_auth_policy_list):
            query['withAuthPolicyList'] = request.with_auth_policy_list
        if not DaraCore.is_null(request.with_consumer_info_by_id):
            query['withConsumerInfoById'] = request.with_consumer_info_by_id
        if not DaraCore.is_null(request.with_environment_info):
            query['withEnvironmentInfo'] = request.with_environment_info
        if not DaraCore.is_null(request.with_environment_info_by_id):
            query['withEnvironmentInfoById'] = request.with_environment_info_by_id
        if not DaraCore.is_null(request.with_ingress_info):
            query['withIngressInfo'] = request.with_ingress_info
        if not DaraCore.is_null(request.with_plugin_attachment_by_plugin_id):
            query['withPluginAttachmentByPluginId'] = request.with_plugin_attachment_by_plugin_id
        if not DaraCore.is_null(request.with_policy_configs):
            query['withPolicyConfigs'] = request.with_policy_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHttpApis',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHttpApisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_http_apis(
        self,
        request: main_models.ListHttpApisRequest,
    ) -> main_models.ListHttpApisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_http_apis_with_options(request, headers, runtime)

    async def list_http_apis_async(
        self,
        request: main_models.ListHttpApisRequest,
    ) -> main_models.ListHttpApisResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_http_apis_with_options_async(request, headers, runtime)

    def list_installable_gateways_with_options(
        self,
        plugin_class_id: str,
        request: main_models.ListInstallableGatewaysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstallableGatewaysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstallableGateways',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-classes/{DaraURL.percent_encode(plugin_class_id)}/installable-gateways',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstallableGatewaysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_installable_gateways_with_options_async(
        self,
        plugin_class_id: str,
        request: main_models.ListInstallableGatewaysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstallableGatewaysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstallableGateways',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-classes/{DaraURL.percent_encode(plugin_class_id)}/installable-gateways',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstallableGatewaysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_installable_gateways(
        self,
        plugin_class_id: str,
        request: main_models.ListInstallableGatewaysRequest,
    ) -> main_models.ListInstallableGatewaysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_installable_gateways_with_options(plugin_class_id, request, headers, runtime)

    async def list_installable_gateways_async(
        self,
        plugin_class_id: str,
        request: main_models.ListInstallableGatewaysRequest,
    ) -> main_models.ListInstallableGatewaysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_installable_gateways_with_options_async(plugin_class_id, request, headers, runtime)

    def list_k8s_cluster_sources_with_options(
        self,
        gateway_id: str,
        request: main_models.ListK8sClusterSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sClusterSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sClusterSources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/gateways/{DaraURL.percent_encode(gateway_id)}/service-sources/k8s-clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sClusterSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_k8s_cluster_sources_with_options_async(
        self,
        gateway_id: str,
        request: main_models.ListK8sClusterSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListK8sClusterSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vpc_id):
            query['vpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListK8sClusterSources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/gateways/{DaraURL.percent_encode(gateway_id)}/service-sources/k8s-clusters',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListK8sClusterSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_k8s_cluster_sources(
        self,
        gateway_id: str,
        request: main_models.ListK8sClusterSourcesRequest,
    ) -> main_models.ListK8sClusterSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_k8s_cluster_sources_with_options(gateway_id, request, headers, runtime)

    async def list_k8s_cluster_sources_async(
        self,
        gateway_id: str,
        request: main_models.ListK8sClusterSourcesRequest,
    ) -> main_models.ListK8sClusterSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_k8s_cluster_sources_with_options_async(gateway_id, request, headers, runtime)

    def list_mcp_servers_with_options(
        self,
        request: main_models.ListMcpServersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_from_types):
            query['createFromTypes'] = request.create_from_types
        if not DaraCore.is_null(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMcpServers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mcp_servers_with_options_async(
        self,
        request: main_models.ListMcpServersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMcpServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_from_types):
            query['createFromTypes'] = request.create_from_types
        if not DaraCore.is_null(request.deploy_statuses):
            query['deployStatuses'] = request.deploy_statuses
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMcpServers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMcpServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mcp_servers(
        self,
        request: main_models.ListMcpServersRequest,
    ) -> main_models.ListMcpServersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mcp_servers_with_options(request, headers, runtime)

    async def list_mcp_servers_async(
        self,
        request: main_models.ListMcpServersRequest,
    ) -> main_models.ListMcpServersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mcp_servers_with_options_async(request, headers, runtime)

    def list_migration_tasks_with_options(
        self,
        request: main_models.ListMigrationTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMigrationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMigrationTasks',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMigrationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_migration_tasks_with_options_async(
        self,
        request: main_models.ListMigrationTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMigrationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMigrationTasks',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMigrationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_migration_tasks(
        self,
        request: main_models.ListMigrationTasksRequest,
    ) -> main_models.ListMigrationTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_migration_tasks_with_options(request, headers, runtime)

    async def list_migration_tasks_async(
        self,
        request: main_models.ListMigrationTasksRequest,
    ) -> main_models.ListMigrationTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_migration_tasks_with_options_async(request, headers, runtime)

    def list_mse_nacos_sources_with_options(
        self,
        gateway_id: str,
        request: main_models.ListMseNacosSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMseNacosSourcesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListMseNacosSources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/service-sources/mse-nacos-instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMseNacosSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mse_nacos_sources_with_options_async(
        self,
        gateway_id: str,
        request: main_models.ListMseNacosSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMseNacosSourcesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListMseNacosSources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/service-sources/mse-nacos-instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMseNacosSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mse_nacos_sources(
        self,
        gateway_id: str,
        request: main_models.ListMseNacosSourcesRequest,
    ) -> main_models.ListMseNacosSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mse_nacos_sources_with_options(gateway_id, request, headers, runtime)

    async def list_mse_nacos_sources_async(
        self,
        gateway_id: str,
        request: main_models.ListMseNacosSourcesRequest,
    ) -> main_models.ListMseNacosSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mse_nacos_sources_with_options_async(gateway_id, request, headers, runtime)

    def list_plugin_attachments_with_options(
        self,
        request: main_models.ListPluginAttachmentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.attach_resource_types):
            query['attachResourceTypes'] = request.attach_resource_types
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.with_parent_resource):
            query['withParentResource'] = request.with_parent_resource
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPluginAttachments',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugin_attachments_with_options_async(
        self,
        request: main_models.ListPluginAttachmentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginAttachmentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.attach_resource_types):
            query['attachResourceTypes'] = request.attach_resource_types
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_id):
            query['pluginId'] = request.plugin_id
        if not DaraCore.is_null(request.with_parent_resource):
            query['withParentResource'] = request.with_parent_resource
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPluginAttachments',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugin_attachments(
        self,
        request: main_models.ListPluginAttachmentsRequest,
    ) -> main_models.ListPluginAttachmentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_plugin_attachments_with_options(request, headers, runtime)

    async def list_plugin_attachments_async(
        self,
        request: main_models.ListPluginAttachmentsRequest,
    ) -> main_models.ListPluginAttachmentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_plugin_attachments_with_options_async(request, headers, runtime)

    def list_plugin_classes_with_options(
        self,
        request: main_models.ListPluginClassesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginClassesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_like):
            query['aliasLike'] = request.alias_like
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.exclude_builtin_ai_proxy):
            query['excludeBuiltinAiProxy'] = request.exclude_builtin_ai_proxy
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.installed):
            query['installed'] = request.installed
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPluginClasses',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-classes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginClassesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugin_classes_with_options_async(
        self,
        request: main_models.ListPluginClassesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginClassesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_like):
            query['aliasLike'] = request.alias_like
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.exclude_builtin_ai_proxy):
            query['excludeBuiltinAiProxy'] = request.exclude_builtin_ai_proxy
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.installed):
            query['installed'] = request.installed
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.source):
            query['source'] = request.source
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPluginClasses',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-classes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginClassesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugin_classes(
        self,
        request: main_models.ListPluginClassesRequest,
    ) -> main_models.ListPluginClassesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_plugin_classes_with_options(request, headers, runtime)

    async def list_plugin_classes_async(
        self,
        request: main_models.ListPluginClassesRequest,
    ) -> main_models.ListPluginClassesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_plugin_classes_with_options_async(request, headers, runtime)

    def list_plugin_repositories_with_options(
        self,
        request: main_models.ListPluginRepositoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginRepositoriesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPluginRepositories',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-repositories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugin_repositories_with_options_async(
        self,
        request: main_models.ListPluginRepositoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginRepositoriesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPluginRepositories',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-repositories',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugin_repositories(
        self,
        request: main_models.ListPluginRepositoriesRequest,
    ) -> main_models.ListPluginRepositoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_plugin_repositories_with_options(request, headers, runtime)

    async def list_plugin_repositories_async(
        self,
        request: main_models.ListPluginRepositoriesRequest,
    ) -> main_models.ListPluginRepositoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_plugin_repositories_with_options_async(request, headers, runtime)

    def list_plugin_workspace_with_options(
        self,
        request: main_models.ListPluginWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPluginWorkspace',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugin_workspace_with_options_async(
        self,
        request: main_models.ListPluginWorkspaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPluginWorkspace',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-workspaces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugin_workspace(
        self,
        request: main_models.ListPluginWorkspaceRequest,
    ) -> main_models.ListPluginWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_plugin_workspace_with_options(request, headers, runtime)

    async def list_plugin_workspace_async(
        self,
        request: main_models.ListPluginWorkspaceRequest,
    ) -> main_models.ListPluginWorkspaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_plugin_workspace_with_options_async(request, headers, runtime)

    def list_plugins_with_options(
        self,
        request: main_models.ListPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.include_builtin_ai_gateway):
            query['includeBuiltinAiGateway'] = request.include_builtin_ai_gateway
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not DaraCore.is_null(request.plugin_class_name):
            query['pluginClassName'] = request.plugin_class_name
        if not DaraCore.is_null(request.with_attachment_info):
            query['withAttachmentInfo'] = request.with_attachment_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPlugins',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_plugins_with_options_async(
        self,
        request: main_models.ListPluginsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPluginsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.include_builtin_ai_gateway):
            query['includeBuiltinAiGateway'] = request.include_builtin_ai_gateway
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.plugin_class_id):
            query['pluginClassId'] = request.plugin_class_id
        if not DaraCore.is_null(request.plugin_class_name):
            query['pluginClassName'] = request.plugin_class_name
        if not DaraCore.is_null(request.with_attachment_info):
            query['withAttachmentInfo'] = request.with_attachment_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPlugins',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPluginsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_plugins(
        self,
        request: main_models.ListPluginsRequest,
    ) -> main_models.ListPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_plugins_with_options(request, headers, runtime)

    async def list_plugins_async(
        self,
        request: main_models.ListPluginsRequest,
    ) -> main_models.ListPluginsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_plugins_with_options_async(request, headers, runtime)

    def list_policies_with_options(
        self,
        request: main_models.ListPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.with_attachments):
            query['withAttachments'] = request.with_attachments
        if not DaraCore.is_null(request.with_system_policy):
            query['withSystemPolicy'] = request.with_system_policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: main_models.ListPoliciesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.with_attachments):
            query['withAttachments'] = request.with_attachments
        if not DaraCore.is_null(request.with_system_policy):
            query['withSystemPolicy'] = request.with_system_policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_policies_with_options(request, headers, runtime)

    async def list_policies_async(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_policies_with_options_async(request, headers, runtime)

    def list_policy_classes_with_options(
        self,
        request: main_models.ListPolicyClassesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyClassesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyClasses',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-classes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyClassesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_classes_with_options_async(
        self,
        request: main_models.ListPolicyClassesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicyClassesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_resource_id):
            query['attachResourceId'] = request.attach_resource_id
        if not DaraCore.is_null(request.attach_resource_type):
            query['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.direction):
            query['direction'] = request.direction
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicyClasses',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policy-classes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicyClassesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_classes(
        self,
        request: main_models.ListPolicyClassesRequest,
    ) -> main_models.ListPolicyClassesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_policy_classes_with_options(request, headers, runtime)

    async def list_policy_classes_async(
        self,
        request: main_models.ListPolicyClassesRequest,
    ) -> main_models.ListPolicyClassesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_policy_classes_with_options_async(request, headers, runtime)

    def list_risk_check_results_with_options(
        self,
        gateway_id: str,
        request: main_models.ListRiskCheckResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRiskCheckResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRiskCheckResults',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/risk-check/results',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRiskCheckResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_risk_check_results_with_options_async(
        self,
        gateway_id: str,
        request: main_models.ListRiskCheckResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRiskCheckResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRiskCheckResults',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/risk-check/results',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRiskCheckResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_risk_check_results(
        self,
        gateway_id: str,
        request: main_models.ListRiskCheckResultsRequest,
    ) -> main_models.ListRiskCheckResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_risk_check_results_with_options(gateway_id, request, headers, runtime)

    async def list_risk_check_results_async(
        self,
        gateway_id: str,
        request: main_models.ListRiskCheckResultsRequest,
    ) -> main_models.ListRiskCheckResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_risk_check_results_with_options_async(gateway_id, request, headers, runtime)

    def list_secret_references_with_options(
        self,
        secret_id: str,
        request: main_models.ListSecretReferencesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretReferencesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecretReferences',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets/{DaraURL.percent_encode(secret_id)}/references',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretReferencesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secret_references_with_options_async(
        self,
        secret_id: str,
        request: main_models.ListSecretReferencesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretReferencesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecretReferences',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets/{DaraURL.percent_encode(secret_id)}/references',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretReferencesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secret_references(
        self,
        secret_id: str,
        request: main_models.ListSecretReferencesRequest,
    ) -> main_models.ListSecretReferencesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_secret_references_with_options(secret_id, request, headers, runtime)

    async def list_secret_references_async(
        self,
        secret_id: str,
        request: main_models.ListSecretReferencesRequest,
    ) -> main_models.ListSecretReferencesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_secret_references_with_options_async(secret_id, request, headers, runtime)

    def list_secrets_with_options(
        self,
        request: main_models.ListSecretsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecrets',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secrets_with_options_async(
        self,
        request: main_models.ListSecretsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_type):
            query['gatewayType'] = request.gateway_type
        if not DaraCore.is_null(request.name_like):
            query['nameLike'] = request.name_like
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecrets',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secrets(
        self,
        request: main_models.ListSecretsRequest,
    ) -> main_models.ListSecretsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_secrets_with_options(request, headers, runtime)

    async def list_secrets_async(
        self,
        request: main_models.ListSecretsRequest,
    ) -> main_models.ListSecretsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_secrets_with_options_async(request, headers, runtime)

    def list_services_with_options(
        self,
        request: main_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.source_types):
            query['sourceTypes'] = request.source_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: main_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.source_types):
            query['sourceTypes'] = request.source_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    async def list_services_async(
        self,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(request, headers, runtime)

    def list_sources_with_options(
        self,
        request: main_models.ListSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sources_with_options_async(
        self,
        request: main_models.ListSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/sources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sources(
        self,
        request: main_models.ListSourcesRequest,
    ) -> main_models.ListSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sources_with_options(request, headers, runtime)

    async def list_sources_async(
        self,
        request: main_models.ListSourcesRequest,
    ) -> main_models.ListSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sources_with_options_async(request, headers, runtime)

    def list_ssl_certs_with_options(
        self,
        request: main_models.ListSslCertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSslCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name_like):
            query['certNameLike'] = request.cert_name_like
        if not DaraCore.is_null(request.domain_name):
            query['domainName'] = request.domain_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSslCerts',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ssl/certs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSslCertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ssl_certs_with_options_async(
        self,
        request: main_models.ListSslCertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSslCertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_name_like):
            query['certNameLike'] = request.cert_name_like
        if not DaraCore.is_null(request.domain_name):
            query['domainName'] = request.domain_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSslCerts',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ssl/certs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSslCertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ssl_certs(
        self,
        request: main_models.ListSslCertsRequest,
    ) -> main_models.ListSslCertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_ssl_certs_with_options(request, headers, runtime)

    async def list_ssl_certs_async(
        self,
        request: main_models.ListSslCertsRequest,
    ) -> main_models.ListSslCertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_ssl_certs_with_options_async(request, headers, runtime)

    def list_sync_mcpserver_with_options(
        self,
        request: main_models.ListSyncMCPServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSyncMCPServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.source_id):
            query['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSyncMCPServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/sync-mcp-server/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSyncMCPServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sync_mcpserver_with_options_async(
        self,
        request: main_models.ListSyncMCPServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSyncMCPServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.namespace):
            query['namespace'] = request.namespace
        if not DaraCore.is_null(request.source_id):
            query['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSyncMCPServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/sync-mcp-server/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSyncMCPServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sync_mcpserver(
        self,
        request: main_models.ListSyncMCPServerRequest,
    ) -> main_models.ListSyncMCPServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_sync_mcpserver_with_options(request, headers, runtime)

    async def list_sync_mcpserver_async(
        self,
        request: main_models.ListSyncMCPServerRequest,
    ) -> main_models.ListSyncMCPServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_sync_mcpserver_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_zones_with_options(
        self,
        request: main_models.ListZonesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_edition):
            query['gatewayEdition'] = request.gateway_edition
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListZones',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/zones',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_zones_with_options_async(
        self,
        request: main_models.ListZonesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gateway_edition):
            query['gatewayEdition'] = request.gateway_edition
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListZones',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/zones',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_zones(
        self,
        request: main_models.ListZonesRequest,
    ) -> main_models.ListZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_zones_with_options(request, headers, runtime)

    async def list_zones_async(
        self,
        request: main_models.ListZonesRequest,
    ) -> main_models.ListZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_zones_with_options_async(request, headers, runtime)

    def query_consumer_authorization_rules_with_options(
        self,
        request: main_models.QueryConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryConsumerAuthorizationRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name_like):
            query['apiNameLike'] = request.api_name_like
        if not DaraCore.is_null(request.consumer_group_id):
            query['consumerGroupId'] = request.consumer_group_id
        if not DaraCore.is_null(request.consumer_group_name_like):
            query['consumerGroupNameLike'] = request.consumer_group_name_like
        if not DaraCore.is_null(request.consumer_id):
            query['consumerId'] = request.consumer_id
        if not DaraCore.is_null(request.consumer_name_like):
            query['consumerNameLike'] = request.consumer_name_like
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.group_by_api):
            query['groupByApi'] = request.group_by_api
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_resource_id):
            query['parentResourceId'] = request.parent_resource_id
        if not DaraCore.is_null(request.principal_type):
            query['principalType'] = request.principal_type
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.resource_types):
            query['resourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryConsumerAuthorizationRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConsumerAuthorizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_consumer_authorization_rules_with_options_async(
        self,
        request: main_models.QueryConsumerAuthorizationRulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryConsumerAuthorizationRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name_like):
            query['apiNameLike'] = request.api_name_like
        if not DaraCore.is_null(request.consumer_group_id):
            query['consumerGroupId'] = request.consumer_group_id
        if not DaraCore.is_null(request.consumer_group_name_like):
            query['consumerGroupNameLike'] = request.consumer_group_name_like
        if not DaraCore.is_null(request.consumer_id):
            query['consumerId'] = request.consumer_id
        if not DaraCore.is_null(request.consumer_name_like):
            query['consumerNameLike'] = request.consumer_name_like
        if not DaraCore.is_null(request.environment_id):
            query['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.group_by_api):
            query['groupByApi'] = request.group_by_api
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_resource_id):
            query['parentResourceId'] = request.parent_resource_id
        if not DaraCore.is_null(request.principal_type):
            query['principalType'] = request.principal_type
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.resource_types):
            query['resourceTypes'] = request.resource_types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryConsumerAuthorizationRules',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryConsumerAuthorizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_consumer_authorization_rules(
        self,
        request: main_models.QueryConsumerAuthorizationRulesRequest,
    ) -> main_models.QueryConsumerAuthorizationRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_consumer_authorization_rules_with_options(request, headers, runtime)

    async def query_consumer_authorization_rules_async(
        self,
        request: main_models.QueryConsumerAuthorizationRulesRequest,
    ) -> main_models.QueryConsumerAuthorizationRulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_consumer_authorization_rules_with_options_async(request, headers, runtime)

    def refresh_plugin_oauth_code_with_options(
        self,
        request: main_models.RefreshPluginOAuthCodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RefreshPluginOAuthCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefreshPluginOAuthCode',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-oauth-codes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshPluginOAuthCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_plugin_oauth_code_with_options_async(
        self,
        request: main_models.RefreshPluginOAuthCodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RefreshPluginOAuthCodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefreshPluginOAuthCode',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-oauth-codes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshPluginOAuthCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_plugin_oauth_code(
        self,
        request: main_models.RefreshPluginOAuthCodeRequest,
    ) -> main_models.RefreshPluginOAuthCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.refresh_plugin_oauth_code_with_options(request, headers, runtime)

    async def refresh_plugin_oauth_code_async(
        self,
        request: main_models.RefreshPluginOAuthCodeRequest,
    ) -> main_models.RefreshPluginOAuthCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.refresh_plugin_oauth_code_with_options_async(request, headers, runtime)

    def remove_consumer_authorization_rule_with_options(
        self,
        consumer_authorization_rule_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_consumer_authorization_rule_with_options_async(
        self,
        consumer_authorization_rule_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveConsumerAuthorizationRuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RemoveConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_consumer_authorization_rule(
        self,
        consumer_authorization_rule_id: str,
    ) -> main_models.RemoveConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_consumer_authorization_rule_with_options(consumer_authorization_rule_id, headers, runtime)

    async def remove_consumer_authorization_rule_async(
        self,
        consumer_authorization_rule_id: str,
    ) -> main_models.RemoveConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_consumer_authorization_rule_with_options_async(consumer_authorization_rule_id, headers, runtime)

    def reset_gateway_quota_rule_with_options(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.ResetGatewayQuotaRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetGatewayQuotaRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conflict_hash):
            body['conflictHash'] = request.conflict_hash
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.overwrite):
            body['overwrite'] = request.overwrite
        if not DaraCore.is_null(request.period_multiplier):
            body['periodMultiplier'] = request.period_multiplier
        if not DaraCore.is_null(request.period_type):
            body['periodType'] = request.period_type
        if not DaraCore.is_null(request.quota_limit):
            body['quotaLimit'] = request.quota_limit
        if not DaraCore.is_null(request.timezone):
            body['timezone'] = request.timezone
        if not DaraCore.is_null(request.window_alignment):
            body['windowAlignment'] = request.window_alignment
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetGatewayQuotaRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}/reset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetGatewayQuotaRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_gateway_quota_rule_with_options_async(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.ResetGatewayQuotaRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetGatewayQuotaRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.conflict_hash):
            body['conflictHash'] = request.conflict_hash
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.overwrite):
            body['overwrite'] = request.overwrite
        if not DaraCore.is_null(request.period_multiplier):
            body['periodMultiplier'] = request.period_multiplier
        if not DaraCore.is_null(request.period_type):
            body['periodType'] = request.period_type
        if not DaraCore.is_null(request.quota_limit):
            body['quotaLimit'] = request.quota_limit
        if not DaraCore.is_null(request.timezone):
            body['timezone'] = request.timezone
        if not DaraCore.is_null(request.window_alignment):
            body['windowAlignment'] = request.window_alignment
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetGatewayQuotaRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}/reset',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetGatewayQuotaRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_gateway_quota_rule(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.ResetGatewayQuotaRuleRequest,
    ) -> main_models.ResetGatewayQuotaRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reset_gateway_quota_rule_with_options(gateway_id, rule_id, request, headers, runtime)

    async def reset_gateway_quota_rule_async(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.ResetGatewayQuotaRuleRequest,
    ) -> main_models.ResetGatewayQuotaRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reset_gateway_quota_rule_with_options_async(gateway_id, rule_id, request, headers, runtime)

    def restart_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RestartGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartGatewayResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RestartGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_gateway(
        self,
        gateway_id: str,
    ) -> main_models.RestartGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_gateway_with_options(gateway_id, headers, runtime)

    async def restart_gateway_async(
        self,
        gateway_id: str,
    ) -> main_models.RestartGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_gateway_with_options_async(gateway_id, headers, runtime)

    def run_plugin_pipeline_with_options(
        self,
        workspace_id: str,
        request: main_models.RunPluginPipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunPluginPipelineResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RunPluginPipeline',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-workspaces/{DaraURL.percent_encode(workspace_id)}/pipeline-run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunPluginPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_plugin_pipeline_with_options_async(
        self,
        workspace_id: str,
        request: main_models.RunPluginPipelineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RunPluginPipelineResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RunPluginPipeline',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-workspaces/{DaraURL.percent_encode(workspace_id)}/pipeline-run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunPluginPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_plugin_pipeline(
        self,
        workspace_id: str,
        request: main_models.RunPluginPipelineRequest,
    ) -> main_models.RunPluginPipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.run_plugin_pipeline_with_options(workspace_id, request, headers, runtime)

    async def run_plugin_pipeline_async(
        self,
        workspace_id: str,
        request: main_models.RunPluginPipelineRequest,
    ) -> main_models.RunPluginPipelineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.run_plugin_pipeline_with_options_async(workspace_id, request, headers, runtime)

    def sync_mcpservers_with_options(
        self,
        request: main_models.SyncMCPServersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncMCPServersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.nacos_mcp_servers):
            body['nacosMcpServers'] = request.nacos_mcp_servers
        if not DaraCore.is_null(request.namespace):
            body['namespace'] = request.namespace
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncMCPServers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/sync-mcp-server',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncMCPServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_mcpservers_with_options_async(
        self,
        request: main_models.SyncMCPServersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncMCPServersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.nacos_mcp_servers):
            body['nacosMcpServers'] = request.nacos_mcp_servers
        if not DaraCore.is_null(request.namespace):
            body['namespace'] = request.namespace
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncMCPServers',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/sync-mcp-server',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncMCPServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_mcpservers(
        self,
        request: main_models.SyncMCPServersRequest,
    ) -> main_models.SyncMCPServersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.sync_mcpservers_with_options(request, headers, runtime)

    async def sync_mcpservers_async(
        self,
        request: main_models.SyncMCPServersRequest,
    ) -> main_models.SyncMCPServersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.sync_mcpservers_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def un_deploy_mcp_server_with_options(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnDeployMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UnDeployMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}/undeploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnDeployMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_deploy_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnDeployMcpServerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UnDeployMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}/undeploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnDeployMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_deploy_mcp_server(
        self,
        mcp_server_id: str,
    ) -> main_models.UnDeployMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.un_deploy_mcp_server_with_options(mcp_server_id, headers, runtime)

    async def un_deploy_mcp_server_async(
        self,
        mcp_server_id: str,
    ) -> main_models.UnDeployMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.un_deploy_mcp_server_with_options_async(mcp_server_id, headers, runtime)

    def undeploy_http_api_with_options(
        self,
        http_api_id: str,
        request: main_models.UndeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UndeployHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.operation_id):
            body['operationId'] = request.operation_id
        if not DaraCore.is_null(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UndeployHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/undeploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UndeployHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def undeploy_http_api_with_options_async(
        self,
        http_api_id: str,
        request: main_models.UndeployHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UndeployHttpApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.operation_id):
            body['operationId'] = request.operation_id
        if not DaraCore.is_null(request.route_id):
            body['routeId'] = request.route_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UndeployHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/undeploy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UndeployHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def undeploy_http_api(
        self,
        http_api_id: str,
        request: main_models.UndeployHttpApiRequest,
    ) -> main_models.UndeployHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.undeploy_http_api_with_options(http_api_id, request, headers, runtime)

    async def undeploy_http_api_async(
        self,
        http_api_id: str,
        request: main_models.UndeployHttpApiRequest,
    ) -> main_models.UndeployHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.undeploy_http_api_with_options_async(http_api_id, request, headers, runtime)

    def uninstall_plugin_with_options(
        self,
        plugin_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallPluginResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UninstallPlugin',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins/{DaraURL.percent_encode(plugin_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallPluginResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_plugin_with_options_async(
        self,
        plugin_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UninstallPluginResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UninstallPlugin',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugins/{DaraURL.percent_encode(plugin_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallPluginResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_plugin(
        self,
        plugin_id: str,
    ) -> main_models.UninstallPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.uninstall_plugin_with_options(plugin_id, headers, runtime)

    async def uninstall_plugin_async(
        self,
        plugin_id: str,
    ) -> main_models.UninstallPluginResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.uninstall_plugin_with_options_async(plugin_id, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_ai_model_card_with_options(
        self,
        model_card_id: str,
        request: main_models.UpdateAiModelCardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAiModelCardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.available_paths):
            body['availablePaths'] = request.available_paths
        if not DaraCore.is_null(request.credit):
            body['credit'] = request.credit
        if not DaraCore.is_null(request.features):
            body['features'] = request.features
        if not DaraCore.is_null(request.meta):
            body['meta'] = request.meta
        if not DaraCore.is_null(request.model_name):
            body['modelName'] = request.model_name
        if not DaraCore.is_null(request.model_provider):
            body['modelProvider'] = request.model_provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAiModelCard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-cards/{DaraURL.percent_encode(model_card_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAiModelCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ai_model_card_with_options_async(
        self,
        model_card_id: str,
        request: main_models.UpdateAiModelCardRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAiModelCardResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.available_paths):
            body['availablePaths'] = request.available_paths
        if not DaraCore.is_null(request.credit):
            body['credit'] = request.credit
        if not DaraCore.is_null(request.features):
            body['features'] = request.features
        if not DaraCore.is_null(request.meta):
            body['meta'] = request.meta
        if not DaraCore.is_null(request.model_name):
            body['modelName'] = request.model_name
        if not DaraCore.is_null(request.model_provider):
            body['modelProvider'] = request.model_provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAiModelCard',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-cards/{DaraURL.percent_encode(model_card_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAiModelCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ai_model_card(
        self,
        model_card_id: str,
        request: main_models.UpdateAiModelCardRequest,
    ) -> main_models.UpdateAiModelCardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_ai_model_card_with_options(model_card_id, request, headers, runtime)

    async def update_ai_model_card_async(
        self,
        model_card_id: str,
        request: main_models.UpdateAiModelCardRequest,
    ) -> main_models.UpdateAiModelCardResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_ai_model_card_with_options_async(model_card_id, request, headers, runtime)

    def update_ai_model_provider_with_options(
        self,
        model_provider_id: str,
        request: main_models.UpdateAiModelProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAiModelProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.service_ids):
            body['serviceIds'] = request.service_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAiModelProvider',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-providers/{DaraURL.percent_encode(model_provider_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAiModelProviderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ai_model_provider_with_options_async(
        self,
        model_provider_id: str,
        request: main_models.UpdateAiModelProviderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAiModelProviderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.service_ids):
            body['serviceIds'] = request.service_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAiModelProvider',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/ai-model-providers/{DaraURL.percent_encode(model_provider_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAiModelProviderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ai_model_provider(
        self,
        model_provider_id: str,
        request: main_models.UpdateAiModelProviderRequest,
    ) -> main_models.UpdateAiModelProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_ai_model_provider_with_options(model_provider_id, request, headers, runtime)

    async def update_ai_model_provider_async(
        self,
        model_provider_id: str,
        request: main_models.UpdateAiModelProviderRequest,
    ) -> main_models.UpdateAiModelProviderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_ai_model_provider_with_options_async(model_provider_id, request, headers, runtime)

    def update_and_attach_policy_with_options(
        self,
        policy_id: str,
        request: main_models.UpdateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAndAttachPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAndAttachPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAndAttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_and_attach_policy_with_options_async(
        self,
        policy_id: str,
        request: main_models.UpdateAndAttachPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAndAttachPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.attach_resource_type):
            body['attachResourceType'] = request.attach_resource_type
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAndAttachPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAndAttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_and_attach_policy(
        self,
        policy_id: str,
        request: main_models.UpdateAndAttachPolicyRequest,
    ) -> main_models.UpdateAndAttachPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_and_attach_policy_with_options(policy_id, request, headers, runtime)

    async def update_and_attach_policy_async(
        self,
        policy_id: str,
        request: main_models.UpdateAndAttachPolicyRequest,
    ) -> main_models.UpdateAndAttachPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_and_attach_policy_with_options_async(policy_id, request, headers, runtime)

    def update_authorization_rule_with_options(
        self,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAuthorizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resources):
            body['resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_authorization_rule_with_options_async(
        self,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAuthorizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resources):
            body['resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_authorization_rule(
        self,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateAuthorizationRuleRequest,
    ) -> main_models.UpdateAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_authorization_rule_with_options(consumer_authorization_rule_id, request, headers, runtime)

    async def update_authorization_rule_async(
        self,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateAuthorizationRuleRequest,
    ) -> main_models.UpdateAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_authorization_rule_with_options_async(consumer_authorization_rule_id, request, headers, runtime)

    def update_consumer_with_options(
        self,
        consumer_id: str,
        request: main_models.UpdateConsumerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not DaraCore.is_null(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_consumer_with_options_async(
        self,
        consumer_id: str,
        request: main_models.UpdateConsumerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ak_sk_identity_configs):
            body['akSkIdentityConfigs'] = request.ak_sk_identity_configs
        if not DaraCore.is_null(request.apikey_identity_config):
            body['apikeyIdentityConfig'] = request.apikey_identity_config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.jwt_identity_config):
            body['jwtIdentityConfig'] = request.jwt_identity_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_consumer(
        self,
        consumer_id: str,
        request: main_models.UpdateConsumerRequest,
    ) -> main_models.UpdateConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_consumer_with_options(consumer_id, request, headers, runtime)

    async def update_consumer_async(
        self,
        consumer_id: str,
        request: main_models.UpdateConsumerRequest,
    ) -> main_models.UpdateConsumerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_consumer_with_options_async(consumer_id, request, headers, runtime)

    def update_consumer_authorization_rule_with_options(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerAuthorizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not DaraCore.is_null(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not DaraCore.is_null(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerAuthorizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_consumer_authorization_rule_with_options_async(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateConsumerAuthorizationRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerAuthorizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.authorization_resource_infos):
            body['authorizationResourceInfos'] = request.authorization_resource_infos
        if not DaraCore.is_null(request.expire_mode):
            body['expireMode'] = request.expire_mode
        if not DaraCore.is_null(request.expire_timestamp):
            body['expireTimestamp'] = request.expire_timestamp
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerAuthorizationRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumers/{DaraURL.percent_encode(consumer_id)}/authorization-rules/{DaraURL.percent_encode(consumer_authorization_rule_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerAuthorizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_consumer_authorization_rule(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateConsumerAuthorizationRuleRequest,
    ) -> main_models.UpdateConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_consumer_authorization_rule_with_options(consumer_id, consumer_authorization_rule_id, request, headers, runtime)

    async def update_consumer_authorization_rule_async(
        self,
        consumer_id: str,
        consumer_authorization_rule_id: str,
        request: main_models.UpdateConsumerAuthorizationRuleRequest,
    ) -> main_models.UpdateConsumerAuthorizationRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_consumer_authorization_rule_with_options_async(consumer_id, consumer_authorization_rule_id, request, headers, runtime)

    def update_consumer_group_with_options(
        self,
        consumer_group_id: str,
        request: main_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_consumer_group_with_options_async(
        self,
        consumer_group_id: str,
        request: main_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerGroup',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/consumer-groups/{DaraURL.percent_encode(consumer_group_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_consumer_group(
        self,
        consumer_group_id: str,
        request: main_models.UpdateConsumerGroupRequest,
    ) -> main_models.UpdateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(consumer_group_id, request, headers, runtime)

    async def update_consumer_group_async(
        self,
        consumer_group_id: str,
        request: main_models.UpdateConsumerGroupRequest,
    ) -> main_models.UpdateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_consumer_group_with_options_async(consumer_group_id, request, headers, runtime)

    def update_domain_with_options(
        self,
        domain_id: str,
        request: main_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not DaraCore.is_null(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not DaraCore.is_null(request.domain_scope):
            body['domainScope'] = request.domain_scope
        if not DaraCore.is_null(request.force_https):
            body['forceHttps'] = request.force_https
        if not DaraCore.is_null(request.http_2option):
            body['http2Option'] = request.http_2option
        if not DaraCore.is_null(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not DaraCore.is_null(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_domain_with_options_async(
        self,
        domain_id: str,
        request: main_models.UpdateDomainRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDomainResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ca_cert_identifier):
            body['caCertIdentifier'] = request.ca_cert_identifier
        if not DaraCore.is_null(request.cert_identifier):
            body['certIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.client_cacert):
            body['clientCACert'] = request.client_cacert
        if not DaraCore.is_null(request.domain_scope):
            body['domainScope'] = request.domain_scope
        if not DaraCore.is_null(request.force_https):
            body['forceHttps'] = request.force_https
        if not DaraCore.is_null(request.http_2option):
            body['http2Option'] = request.http_2option
        if not DaraCore.is_null(request.m_tlsenabled):
            body['mTLSEnabled'] = request.m_tlsenabled
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.tls_cipher_suites_config):
            body['tlsCipherSuitesConfig'] = request.tls_cipher_suites_config
        if not DaraCore.is_null(request.tls_max):
            body['tlsMax'] = request.tls_max
        if not DaraCore.is_null(request.tls_min):
            body['tlsMin'] = request.tls_min
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDomain',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/domains/{DaraURL.percent_encode(domain_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_domain(
        self,
        domain_id: str,
        request: main_models.UpdateDomainRequest,
    ) -> main_models.UpdateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_domain_with_options(domain_id, request, headers, runtime)

    async def update_domain_async(
        self,
        domain_id: str,
        request: main_models.UpdateDomainRequest,
    ) -> main_models.UpdateDomainResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_domain_with_options_async(domain_id, request, headers, runtime)

    def update_environment_with_options(
        self,
        environment_id: str,
        request: main_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvironmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_with_options_async(
        self,
        environment_id: str,
        request: main_models.UpdateEnvironmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvironmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alias):
            body['alias'] = request.alias
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvironment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/environments/{DaraURL.percent_encode(environment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment(
        self,
        environment_id: str,
        request: main_models.UpdateEnvironmentRequest,
    ) -> main_models.UpdateEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_environment_with_options(environment_id, request, headers, runtime)

    async def update_environment_async(
        self,
        environment_id: str,
        request: main_models.UpdateEnvironmentRequest,
    ) -> main_models.UpdateEnvironmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_environment_with_options_async(environment_id, request, headers, runtime)

    def update_gateway_elastic_policy_with_options(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayElasticPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayElasticPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_policy):
            body['elasticPolicy'] = request.elastic_policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayElasticPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/elastic-policy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayElasticPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_elastic_policy_with_options_async(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayElasticPolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayElasticPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.elastic_policy):
            body['elasticPolicy'] = request.elastic_policy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayElasticPolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/elastic-policy',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayElasticPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_elastic_policy(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayElasticPolicyRequest,
    ) -> main_models.UpdateGatewayElasticPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_elastic_policy_with_options(gateway_id, request, headers, runtime)

    async def update_gateway_elastic_policy_async(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayElasticPolicyRequest,
    ) -> main_models.UpdateGatewayElasticPolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_elastic_policy_with_options_async(gateway_id, request, headers, runtime)

    def update_gateway_feature_with_options(
        self,
        gateway_id: str,
        name: str,
        request: main_models.UpdateGatewayFeatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.value):
            body['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayFeature',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/gateway-features/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_feature_with_options_async(
        self,
        gateway_id: str,
        name: str,
        request: main_models.UpdateGatewayFeatureRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayFeatureResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.value):
            body['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayFeature',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/gateway-features/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_feature(
        self,
        gateway_id: str,
        name: str,
        request: main_models.UpdateGatewayFeatureRequest,
    ) -> main_models.UpdateGatewayFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_feature_with_options(gateway_id, name, request, headers, runtime)

    async def update_gateway_feature_async(
        self,
        gateway_id: str,
        name: str,
        request: main_models.UpdateGatewayFeatureRequest,
    ) -> main_models.UpdateGatewayFeatureResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_feature_with_options_async(gateway_id, name, request, headers, runtime)

    def update_gateway_load_balancer_with_options(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayLoadBalancerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayLoadBalancerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.load_balancer_dto):
            body['loadBalancerDTO'] = request.load_balancer_dto
        if not DaraCore.is_null(request.option):
            body['option'] = request.option
        if not DaraCore.is_null(request.ports):
            body['ports'] = request.ports
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayLoadBalancer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/update-load-balancer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_load_balancer_with_options_async(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayLoadBalancerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayLoadBalancerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.load_balancer_dto):
            body['loadBalancerDTO'] = request.load_balancer_dto
        if not DaraCore.is_null(request.option):
            body['option'] = request.option
        if not DaraCore.is_null(request.ports):
            body['ports'] = request.ports
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayLoadBalancer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/update-load-balancer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayLoadBalancerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_load_balancer(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayLoadBalancerRequest,
    ) -> main_models.UpdateGatewayLoadBalancerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_load_balancer_with_options(gateway_id, request, headers, runtime)

    async def update_gateway_load_balancer_async(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayLoadBalancerRequest,
    ) -> main_models.UpdateGatewayLoadBalancerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_load_balancer_with_options_async(gateway_id, request, headers, runtime)

    def update_gateway_maintenance_period_with_options(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayMaintenancePeriodRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayMaintenancePeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.maintenance_period):
            body['maintenancePeriod'] = request.maintenance_period
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayMaintenancePeriod',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/maintenance-period',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayMaintenancePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_maintenance_period_with_options_async(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayMaintenancePeriodRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayMaintenancePeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.maintenance_period):
            body['maintenancePeriod'] = request.maintenance_period
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayMaintenancePeriod',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/maintenance-period',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayMaintenancePeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_maintenance_period(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayMaintenancePeriodRequest,
    ) -> main_models.UpdateGatewayMaintenancePeriodResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_maintenance_period_with_options(gateway_id, request, headers, runtime)

    async def update_gateway_maintenance_period_async(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayMaintenancePeriodRequest,
    ) -> main_models.UpdateGatewayMaintenancePeriodResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_maintenance_period_with_options_async(gateway_id, request, headers, runtime)

    def update_gateway_name_with_options(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayName',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/name',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_name_with_options_async(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayName',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/name',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_name(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayNameRequest,
    ) -> main_models.UpdateGatewayNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_name_with_options(gateway_id, request, headers, runtime)

    async def update_gateway_name_async(
        self,
        gateway_id: str,
        request: main_models.UpdateGatewayNameRequest,
    ) -> main_models.UpdateGatewayNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_name_with_options_async(gateway_id, request, headers, runtime)

    def update_gateway_quota_rule_with_options(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.UpdateGatewayQuotaRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayQuotaRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.add_ids):
            body['addIds'] = request.add_ids
        if not DaraCore.is_null(request.conflict_hash):
            body['conflictHash'] = request.conflict_hash
        if not DaraCore.is_null(request.consumer_group_ids):
            body['consumerGroupIds'] = request.consumer_group_ids
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.overwrite):
            body['overwrite'] = request.overwrite
        if not DaraCore.is_null(request.quota_limit):
            body['quotaLimit'] = request.quota_limit
        if not DaraCore.is_null(request.remove_ids):
            body['removeIds'] = request.remove_ids
        if not DaraCore.is_null(request.rule_name):
            body['ruleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayQuotaRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayQuotaRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_quota_rule_with_options_async(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.UpdateGatewayQuotaRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayQuotaRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.add_ids):
            body['addIds'] = request.add_ids
        if not DaraCore.is_null(request.conflict_hash):
            body['conflictHash'] = request.conflict_hash
        if not DaraCore.is_null(request.consumer_group_ids):
            body['consumerGroupIds'] = request.consumer_group_ids
        if not DaraCore.is_null(request.dry_run):
            body['dryRun'] = request.dry_run
        if not DaraCore.is_null(request.overwrite):
            body['overwrite'] = request.overwrite
        if not DaraCore.is_null(request.quota_limit):
            body['quotaLimit'] = request.quota_limit
        if not DaraCore.is_null(request.remove_ids):
            body['removeIds'] = request.remove_ids
        if not DaraCore.is_null(request.rule_name):
            body['ruleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayQuotaRule',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayQuotaRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_quota_rule(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.UpdateGatewayQuotaRuleRequest,
    ) -> main_models.UpdateGatewayQuotaRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_quota_rule_with_options(gateway_id, rule_id, request, headers, runtime)

    async def update_gateway_quota_rule_async(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.UpdateGatewayQuotaRuleRequest,
    ) -> main_models.UpdateGatewayQuotaRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_quota_rule_with_options_async(gateway_id, rule_id, request, headers, runtime)

    def update_gateway_quota_rule_status_with_options(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.UpdateGatewayQuotaRuleStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayQuotaRuleStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clear_history):
            body['clearHistory'] = request.clear_history
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayQuotaRuleStatus',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}/status',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayQuotaRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_quota_rule_status_with_options_async(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.UpdateGatewayQuotaRuleStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGatewayQuotaRuleStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.clear_history):
            body['clearHistory'] = request.clear_history
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGatewayQuotaRuleStatus',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/quota-rules/{DaraURL.percent_encode(rule_id)}/status',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGatewayQuotaRuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_quota_rule_status(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.UpdateGatewayQuotaRuleStatusRequest,
    ) -> main_models.UpdateGatewayQuotaRuleStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_gateway_quota_rule_status_with_options(gateway_id, rule_id, request, headers, runtime)

    async def update_gateway_quota_rule_status_async(
        self,
        gateway_id: str,
        rule_id: str,
        request: main_models.UpdateGatewayQuotaRuleStatusRequest,
    ) -> main_models.UpdateGatewayQuotaRuleStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_gateway_quota_rule_status_with_options_async(gateway_id, rule_id, request, headers, runtime)

    def update_http_api_with_options(
        self,
        http_api_id: str,
        request: main_models.UpdateHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not DaraCore.is_null(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not DaraCore.is_null(request.auth_config):
            body['authConfig'] = request.auth_config
        if not DaraCore.is_null(request.base_path):
            body['basePath'] = request.base_path
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not DaraCore.is_null(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not DaraCore.is_null(request.only_change_config):
            body['onlyChangeConfig'] = request.only_change_config
        if not DaraCore.is_null(request.protocols):
            body['protocols'] = request.protocols
        if not DaraCore.is_null(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_with_options_async(
        self,
        http_api_id: str,
        request: main_models.UpdateHttpApiRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not DaraCore.is_null(request.agent_protocols):
            body['agentProtocols'] = request.agent_protocols
        if not DaraCore.is_null(request.ai_protocols):
            body['aiProtocols'] = request.ai_protocols
        if not DaraCore.is_null(request.auth_config):
            body['authConfig'] = request.auth_config
        if not DaraCore.is_null(request.base_path):
            body['basePath'] = request.base_path
        if not DaraCore.is_null(request.deploy_configs):
            body['deployConfigs'] = request.deploy_configs
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.enable_auth):
            body['enableAuth'] = request.enable_auth
        if not DaraCore.is_null(request.first_byte_timeout):
            body['firstByteTimeout'] = request.first_byte_timeout
        if not DaraCore.is_null(request.ingress_config):
            body['ingressConfig'] = request.ingress_config
        if not DaraCore.is_null(request.only_change_config):
            body['onlyChangeConfig'] = request.only_change_config
        if not DaraCore.is_null(request.protocols):
            body['protocols'] = request.protocols
        if not DaraCore.is_null(request.remove_base_path_on_forward):
            body['removeBasePathOnForward'] = request.remove_base_path_on_forward
        if not DaraCore.is_null(request.version_config):
            body['versionConfig'] = request.version_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApi',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api(
        self,
        http_api_id: str,
        request: main_models.UpdateHttpApiRequest,
    ) -> main_models.UpdateHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_http_api_with_options(http_api_id, request, headers, runtime)

    async def update_http_api_async(
        self,
        http_api_id: str,
        request: main_models.UpdateHttpApiRequest,
    ) -> main_models.UpdateHttpApiResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_http_api_with_options_async(http_api_id, request, headers, runtime)

    def update_http_api_operation_with_options(
        self,
        http_api_id: str,
        operation_id: str,
        request: main_models.UpdateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operation):
            body['operation'] = request.operation
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_operation_with_options_async(
        self,
        http_api_id: str,
        operation_id: str,
        request: main_models.UpdateHttpApiOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operation):
            body['operation'] = request.operation
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApiOperation',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/operations/{DaraURL.percent_encode(operation_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api_operation(
        self,
        http_api_id: str,
        operation_id: str,
        request: main_models.UpdateHttpApiOperationRequest,
    ) -> main_models.UpdateHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_http_api_operation_with_options(http_api_id, operation_id, request, headers, runtime)

    async def update_http_api_operation_async(
        self,
        http_api_id: str,
        operation_id: str,
        request: main_models.UpdateHttpApiOperationRequest,
    ) -> main_models.UpdateHttpApiOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_http_api_operation_with_options_async(http_api_id, operation_id, request, headers, runtime)

    def update_http_api_route_with_options(
        self,
        http_api_id: str,
        route_id: str,
        request: main_models.UpdateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not DaraCore.is_null(request.policy_configs):
            body['policyConfigs'] = request.policy_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_http_api_route_with_options_async(
        self,
        http_api_id: str,
        route_id: str,
        request: main_models.UpdateHttpApiRouteRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHttpApiRouteResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.environment_id):
            body['environmentId'] = request.environment_id
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_route_config):
            body['mcpRouteConfig'] = request.mcp_route_config
        if not DaraCore.is_null(request.policy_configs):
            body['policyConfigs'] = request.policy_configs
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHttpApiRoute',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/http-apis/{DaraURL.percent_encode(http_api_id)}/routes/{DaraURL.percent_encode(route_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHttpApiRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_http_api_route(
        self,
        http_api_id: str,
        route_id: str,
        request: main_models.UpdateHttpApiRouteRequest,
    ) -> main_models.UpdateHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_http_api_route_with_options(http_api_id, route_id, request, headers, runtime)

    async def update_http_api_route_async(
        self,
        http_api_id: str,
        route_id: str,
        request: main_models.UpdateHttpApiRouteRequest,
    ) -> main_models.UpdateHttpApiRouteResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_http_api_route_with_options_async(http_api_id, route_id, request, headers, runtime)

    def update_mcp_server_with_options(
        self,
        mcp_server_id: str,
        request: main_models.UpdateMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcpServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.create_from_type):
            body['createFromType'] = request.create_from_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not DaraCore.is_null(request.gray_mcp_server_configs):
            body['grayMcpServerConfigs'] = request.gray_mcp_server_configs
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_server_config):
            body['mcpServerConfig'] = request.mcp_server_config
        if not DaraCore.is_null(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mcp_server_with_options_async(
        self,
        mcp_server_id: str,
        request: main_models.UpdateMcpServerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMcpServerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assembled_sources):
            body['assembledSources'] = request.assembled_sources
        if not DaraCore.is_null(request.backend_config):
            body['backendConfig'] = request.backend_config
        if not DaraCore.is_null(request.create_from_type):
            body['createFromType'] = request.create_from_type
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.domain_ids):
            body['domainIds'] = request.domain_ids
        if not DaraCore.is_null(request.exposed_uri_path):
            body['exposedUriPath'] = request.exposed_uri_path
        if not DaraCore.is_null(request.gray_mcp_server_configs):
            body['grayMcpServerConfigs'] = request.gray_mcp_server_configs
        if not DaraCore.is_null(request.match):
            body['match'] = request.match
        if not DaraCore.is_null(request.mcp_server_config):
            body['mcpServerConfig'] = request.mcp_server_config
        if not DaraCore.is_null(request.mcp_statistics_enable):
            body['mcpStatisticsEnable'] = request.mcp_statistics_enable
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMcpServer',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/mcp-servers/{DaraURL.percent_encode(mcp_server_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mcp_server(
        self,
        mcp_server_id: str,
        request: main_models.UpdateMcpServerRequest,
    ) -> main_models.UpdateMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_mcp_server_with_options(mcp_server_id, request, headers, runtime)

    async def update_mcp_server_async(
        self,
        mcp_server_id: str,
        request: main_models.UpdateMcpServerRequest,
    ) -> main_models.UpdateMcpServerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_mcp_server_with_options_async(mcp_server_id, request, headers, runtime)

    def update_migration_task_with_options(
        self,
        task_id: str,
        request: main_models.UpdateMigrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMigrationTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_namespace):
            body['clusterNamespace'] = request.cluster_namespace
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.service_name):
            body['serviceName'] = request.service_name
        if not DaraCore.is_null(request.slb_id):
            body['slbId'] = request.slb_id
        if not DaraCore.is_null(request.switch_type):
            body['switchType'] = request.switch_type
        if not DaraCore.is_null(request.target):
            body['target'] = request.target
        if not DaraCore.is_null(request.virtual_services):
            body['virtualServices'] = request.virtual_services
        if not DaraCore.is_null(request.weight):
            body['weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMigrationTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_migration_task_with_options_async(
        self,
        task_id: str,
        request: main_models.UpdateMigrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMigrationTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_namespace):
            body['clusterNamespace'] = request.cluster_namespace
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.service_name):
            body['serviceName'] = request.service_name
        if not DaraCore.is_null(request.slb_id):
            body['slbId'] = request.slb_id
        if not DaraCore.is_null(request.switch_type):
            body['switchType'] = request.switch_type
        if not DaraCore.is_null(request.target):
            body['target'] = request.target
        if not DaraCore.is_null(request.virtual_services):
            body['virtualServices'] = request.virtual_services
        if not DaraCore.is_null(request.weight):
            body['weight'] = request.weight
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMigrationTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks/{DaraURL.percent_encode(task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMigrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_migration_task(
        self,
        task_id: str,
        request: main_models.UpdateMigrationTaskRequest,
    ) -> main_models.UpdateMigrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_migration_task_with_options(task_id, request, headers, runtime)

    async def update_migration_task_async(
        self,
        task_id: str,
        request: main_models.UpdateMigrationTaskRequest,
    ) -> main_models.UpdateMigrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_migration_task_with_options_async(task_id, request, headers, runtime)

    def update_network_access_with_options(
        self,
        gateway_id: str,
        request: main_models.UpdateNetworkAccessRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetworkAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_access_type):
            query['networkAccessType'] = request.network_access_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetworkAccess',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/network-type',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetworkAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_network_access_with_options_async(
        self,
        gateway_id: str,
        request: main_models.UpdateNetworkAccessRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNetworkAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.network_access_type):
            query['networkAccessType'] = request.network_access_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNetworkAccess',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/network-type',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNetworkAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_network_access(
        self,
        gateway_id: str,
        request: main_models.UpdateNetworkAccessRequest,
    ) -> main_models.UpdateNetworkAccessResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_network_access_with_options(gateway_id, request, headers, runtime)

    async def update_network_access_async(
        self,
        gateway_id: str,
        request: main_models.UpdateNetworkAccessRequest,
    ) -> main_models.UpdateNetworkAccessResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_network_access_with_options_async(gateway_id, request, headers, runtime)

    def update_plugin_attachment_with_options(
        self,
        plugin_attachment_id: str,
        request: main_models.UpdatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePluginAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePluginAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_plugin_attachment_with_options_async(
        self,
        plugin_attachment_id: str,
        request: main_models.UpdatePluginAttachmentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePluginAttachmentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.attach_resource_ids):
            body['attachResourceIds'] = request.attach_resource_ids
        if not DaraCore.is_null(request.enable):
            body['enable'] = request.enable
        if not DaraCore.is_null(request.plugin_config):
            body['pluginConfig'] = request.plugin_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePluginAttachment',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/plugin-attachments/{DaraURL.percent_encode(plugin_attachment_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePluginAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_plugin_attachment(
        self,
        plugin_attachment_id: str,
        request: main_models.UpdatePluginAttachmentRequest,
    ) -> main_models.UpdatePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_plugin_attachment_with_options(plugin_attachment_id, request, headers, runtime)

    async def update_plugin_attachment_async(
        self,
        plugin_attachment_id: str,
        request: main_models.UpdatePluginAttachmentRequest,
    ) -> main_models.UpdatePluginAttachmentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_plugin_attachment_with_options_async(plugin_attachment_id, request, headers, runtime)

    def update_policy_with_options(
        self,
        policy_id: str,
        request: main_models.UpdatePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_with_options_async(
        self,
        policy_id: str,
        request: main_models.UpdatePolicyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicy',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v2/policies/{DaraURL.percent_encode(policy_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy(
        self,
        policy_id: str,
        request: main_models.UpdatePolicyRequest,
    ) -> main_models.UpdatePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_policy_with_options(policy_id, request, headers, runtime)

    async def update_policy_async(
        self,
        policy_id: str,
        request: main_models.UpdatePolicyRequest,
    ) -> main_models.UpdatePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_policy_with_options_async(policy_id, request, headers, runtime)

    def update_risk_notification_with_options(
        self,
        gateway_id: str,
        request: main_models.UpdateRiskNotificationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRiskNotificationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_mute):
            body['isMute'] = request.is_mute
        if not DaraCore.is_null(request.risk_code):
            body['riskCode'] = request.risk_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRiskNotification',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/risk-check/notifications',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRiskNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_risk_notification_with_options_async(
        self,
        gateway_id: str,
        request: main_models.UpdateRiskNotificationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRiskNotificationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_mute):
            body['isMute'] = request.is_mute
        if not DaraCore.is_null(request.risk_code):
            body['riskCode'] = request.risk_code
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRiskNotification',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/risk-check/notifications',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRiskNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_risk_notification(
        self,
        gateway_id: str,
        request: main_models.UpdateRiskNotificationRequest,
    ) -> main_models.UpdateRiskNotificationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_risk_notification_with_options(gateway_id, request, headers, runtime)

    async def update_risk_notification_async(
        self,
        gateway_id: str,
        request: main_models.UpdateRiskNotificationRequest,
    ) -> main_models.UpdateRiskNotificationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_risk_notification_with_options_async(gateway_id, request, headers, runtime)

    def update_secret_with_options(
        self,
        secret_id: str,
        request: main_models.UpdateSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.secret_data):
            body['secretData'] = request.secret_data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecret',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets/{DaraURL.percent_encode(secret_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_with_options_async(
        self,
        secret_id: str,
        request: main_models.UpdateSecretRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.secret_data):
            body['secretData'] = request.secret_data
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecret',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/secrets/{DaraURL.percent_encode(secret_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret(
        self,
        secret_id: str,
        request: main_models.UpdateSecretRequest,
    ) -> main_models.UpdateSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_secret_with_options(secret_id, request, headers, runtime)

    async def update_secret_async(
        self,
        secret_id: str,
        request: main_models.UpdateSecretRequest,
    ) -> main_models.UpdateSecretResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_secret_with_options_async(secret_id, request, headers, runtime)

    def update_service_with_options(
        self,
        service_id: str,
        request: main_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.addresses):
            body['addresses'] = request.addresses
        if not DaraCore.is_null(request.agent_service_config):
            body['agentServiceConfig'] = request.agent_service_config
        if not DaraCore.is_null(request.ai_service_config):
            body['aiServiceConfig'] = request.ai_service_config
        if not DaraCore.is_null(request.dns_servers):
            body['dnsServers'] = request.dns_servers
        if not DaraCore.is_null(request.health_check_config):
            body['healthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.healthy_panic_threshold):
            body['healthyPanicThreshold'] = request.healthy_panic_threshold
        if not DaraCore.is_null(request.model_provider_id):
            body['modelProviderId'] = request.model_provider_id
        if not DaraCore.is_null(request.outlier_detection_config):
            body['outlierDetectionConfig'] = request.outlier_detection_config
        if not DaraCore.is_null(request.ports):
            body['ports'] = request.ports
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        service_id: str,
        request: main_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.addresses):
            body['addresses'] = request.addresses
        if not DaraCore.is_null(request.agent_service_config):
            body['agentServiceConfig'] = request.agent_service_config
        if not DaraCore.is_null(request.ai_service_config):
            body['aiServiceConfig'] = request.ai_service_config
        if not DaraCore.is_null(request.dns_servers):
            body['dnsServers'] = request.dns_servers
        if not DaraCore.is_null(request.health_check_config):
            body['healthCheckConfig'] = request.health_check_config
        if not DaraCore.is_null(request.healthy_panic_threshold):
            body['healthyPanicThreshold'] = request.healthy_panic_threshold
        if not DaraCore.is_null(request.model_provider_id):
            body['modelProviderId'] = request.model_provider_id
        if not DaraCore.is_null(request.outlier_detection_config):
            body['outlierDetectionConfig'] = request.outlier_detection_config
        if not DaraCore.is_null(request.ports):
            body['ports'] = request.ports
        if not DaraCore.is_null(request.protocol):
            body['protocol'] = request.protocol
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateService',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        service_id: str,
        request: main_models.UpdateServiceRequest,
    ) -> main_models.UpdateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_with_options(service_id, request, headers, runtime)

    async def update_service_async(
        self,
        service_id: str,
        request: main_models.UpdateServiceRequest,
    ) -> main_models.UpdateServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_with_options_async(service_id, request, headers, runtime)

    def update_service_version_with_options(
        self,
        service_id: str,
        name: str,
        request: main_models.UpdateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_version_with_options_async(
        self,
        service_id: str,
        name: str,
        request: main_models.UpdateServiceVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.labels):
            body['labels'] = request.labels
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceVersion',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/services/{DaraURL.percent_encode(service_id)}/versions/{DaraURL.percent_encode(name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_version(
        self,
        service_id: str,
        name: str,
        request: main_models.UpdateServiceVersionRequest,
    ) -> main_models.UpdateServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_service_version_with_options(service_id, name, request, headers, runtime)

    async def update_service_version_async(
        self,
        service_id: str,
        name: str,
        request: main_models.UpdateServiceVersionRequest,
    ) -> main_models.UpdateServiceVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_service_version_with_options_async(service_id, name, request, headers, runtime)

    def upgrade_gateway_with_options(
        self,
        gateway_id: str,
        request: main_models.UpgradeGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/upgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_gateway_with_options_async(
        self,
        gateway_id: str,
        request: main_models.UpgradeGatewayRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeGatewayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeGateway',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/gateways/{DaraURL.percent_encode(gateway_id)}/upgrade',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_gateway(
        self,
        gateway_id: str,
        request: main_models.UpgradeGatewayRequest,
    ) -> main_models.UpgradeGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.upgrade_gateway_with_options(gateway_id, request, headers, runtime)

    async def upgrade_gateway_async(
        self,
        gateway_id: str,
        request: main_models.UpgradeGatewayRequest,
    ) -> main_models.UpgradeGatewayResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.upgrade_gateway_with_options_async(gateway_id, request, headers, runtime)

    def verify_migration_task_with_options(
        self,
        task_id: str,
        request: main_models.VerifyMigrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.VerifyMigrationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'VerifyMigrationTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks/{DaraURL.percent_encode(task_id)}/verify',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyMigrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_migration_task_with_options_async(
        self,
        task_id: str,
        request: main_models.VerifyMigrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.VerifyMigrationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'VerifyMigrationTask',
            version = '2024-03-27',
            protocol = 'HTTPS',
            pathname = f'/v1/migration-tasks/{DaraURL.percent_encode(task_id)}/verify',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyMigrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_migration_task(
        self,
        task_id: str,
        request: main_models.VerifyMigrationTaskRequest,
    ) -> main_models.VerifyMigrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.verify_migration_task_with_options(task_id, request, headers, runtime)

    async def verify_migration_task_async(
        self,
        task_id: str,
        request: main_models.VerifyMigrationTaskRequest,
    ) -> main_models.VerifyMigrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.verify_migration_task_with_options_async(task_id, request, headers, runtime)
