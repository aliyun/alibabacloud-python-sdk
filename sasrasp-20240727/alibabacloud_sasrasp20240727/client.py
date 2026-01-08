# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sasrasp20240727 import models as main_models
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
        self._endpoint = self.get_endpoint('sasrasp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_attack_protection_count_with_options(
        self,
        request: main_models.DescribeAttackProtectionCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAttackProtectionCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAttackProtectionCount',
            version = '2024-07-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAttackProtectionCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attack_protection_count_with_options_async(
        self,
        request: main_models.DescribeAttackProtectionCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAttackProtectionCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAttackProtectionCount',
            version = '2024-07-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAttackProtectionCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attack_protection_count(
        self,
        request: main_models.DescribeAttackProtectionCountRequest,
    ) -> main_models.DescribeAttackProtectionCountResponse:
        runtime = RuntimeOptions()
        return self.describe_attack_protection_count_with_options(request, runtime)

    async def describe_attack_protection_count_async(
        self,
        request: main_models.DescribeAttackProtectionCountRequest,
    ) -> main_models.DescribeAttackProtectionCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_attack_protection_count_with_options_async(request, runtime)

    def describe_attacks_with_options(
        self,
        request: main_models.DescribeAttacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAttacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.attack_host_id):
            query['AttackHostId'] = request.attack_host_id
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.attack_url):
            query['AttackUrl'] = request.attack_url
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.handle_status):
            query['HandleStatus'] = request.handle_status
        if not DaraCore.is_null(request.handler_type):
            query['HandlerType'] = request.handler_type
        if not DaraCore.is_null(request.hostname):
            query['Hostname'] = request.hostname
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.rasp_type):
            query['RaspType'] = request.rasp_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.remote):
            query['Remote'] = request.remote
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not DaraCore.is_null(request.union_id):
            query['UnionId'] = request.union_id
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAttacks',
            version = '2024-07-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAttacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attacks_with_options_async(
        self,
        request: main_models.DescribeAttacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAttacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.application_id):
            query['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.attack_host_id):
            query['AttackHostId'] = request.attack_host_id
        if not DaraCore.is_null(request.attack_type):
            query['AttackType'] = request.attack_type
        if not DaraCore.is_null(request.attack_url):
            query['AttackUrl'] = request.attack_url
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.handle_status):
            query['HandleStatus'] = request.handle_status
        if not DaraCore.is_null(request.handler_type):
            query['HandlerType'] = request.handler_type
        if not DaraCore.is_null(request.hostname):
            query['Hostname'] = request.hostname
        if not DaraCore.is_null(request.ip):
            query['Ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.rasp_type):
            query['RaspType'] = request.rasp_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.remote):
            query['Remote'] = request.remote
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not DaraCore.is_null(request.union_id):
            query['UnionId'] = request.union_id
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAttacks',
            version = '2024-07-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAttacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attacks(
        self,
        request: main_models.DescribeAttacksRequest,
    ) -> main_models.DescribeAttacksResponse:
        runtime = RuntimeOptions()
        return self.describe_attacks_with_options(request, runtime)

    async def describe_attacks_async(
        self,
        request: main_models.DescribeAttacksRequest,
    ) -> main_models.DescribeAttacksResponse:
        runtime = RuntimeOptions()
        return await self.describe_attacks_with_options_async(request, runtime)
