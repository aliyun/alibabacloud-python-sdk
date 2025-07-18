# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sasrasp20240727 import models as sas_rasp_20240727_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_attack_protection_count_with_options(
        self,
        request: sas_rasp_20240727_models.DescribeAttackProtectionCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_rasp_20240727_models.DescribeAttackProtectionCountResponse:
        """
        @summary DescribeAttackProtectionCount
        
        @param request: DescribeAttackProtectionCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAttackProtectionCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_type):
            query['AgentType'] = request.agent_type
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackProtectionCount',
            version='2024-07-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_rasp_20240727_models.DescribeAttackProtectionCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attack_protection_count_with_options_async(
        self,
        request: sas_rasp_20240727_models.DescribeAttackProtectionCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_rasp_20240727_models.DescribeAttackProtectionCountResponse:
        """
        @summary DescribeAttackProtectionCount
        
        @param request: DescribeAttackProtectionCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAttackProtectionCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_type):
            query['AgentType'] = request.agent_type
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAttackProtectionCount',
            version='2024-07-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_rasp_20240727_models.DescribeAttackProtectionCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attack_protection_count(
        self,
        request: sas_rasp_20240727_models.DescribeAttackProtectionCountRequest,
    ) -> sas_rasp_20240727_models.DescribeAttackProtectionCountResponse:
        """
        @summary DescribeAttackProtectionCount
        
        @param request: DescribeAttackProtectionCountRequest
        @return: DescribeAttackProtectionCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_attack_protection_count_with_options(request, runtime)

    async def describe_attack_protection_count_async(
        self,
        request: sas_rasp_20240727_models.DescribeAttackProtectionCountRequest,
    ) -> sas_rasp_20240727_models.DescribeAttackProtectionCountResponse:
        """
        @summary DescribeAttackProtectionCount
        
        @param request: DescribeAttackProtectionCountRequest
        @return: DescribeAttackProtectionCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_attack_protection_count_with_options_async(request, runtime)

    def describe_attacks_with_options(
        self,
        request: sas_rasp_20240727_models.DescribeAttacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_rasp_20240727_models.DescribeAttacksResponse:
        """
        @summary 查询攻击项
        
        @param request: DescribeAttacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAttacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_type):
            query['AgentType'] = request.agent_type
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.attack_host_id):
            query['AttackHostId'] = request.attack_host_id
        if not UtilClient.is_unset(request.attack_type):
            query['AttackType'] = request.attack_type
        if not UtilClient.is_unset(request.attack_url):
            query['AttackUrl'] = request.attack_url
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.handler_type):
            query['HandlerType'] = request.handler_type
        if not UtilClient.is_unset(request.hostname):
            query['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.rasp_type):
            query['RaspType'] = request.rasp_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.remote):
            query['Remote'] = request.remote
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.union_id):
            query['UnionId'] = request.union_id
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAttacks',
            version='2024-07-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_rasp_20240727_models.DescribeAttacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_attacks_with_options_async(
        self,
        request: sas_rasp_20240727_models.DescribeAttacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sas_rasp_20240727_models.DescribeAttacksResponse:
        """
        @summary 查询攻击项
        
        @param request: DescribeAttacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAttacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_type):
            query['AgentType'] = request.agent_type
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.attack_host_id):
            query['AttackHostId'] = request.attack_host_id
        if not UtilClient.is_unset(request.attack_type):
            query['AttackType'] = request.attack_type
        if not UtilClient.is_unset(request.attack_url):
            query['AttackUrl'] = request.attack_url
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.handler_type):
            query['HandlerType'] = request.handler_type
        if not UtilClient.is_unset(request.hostname):
            query['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.rasp_type):
            query['RaspType'] = request.rasp_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.remote):
            query['Remote'] = request.remote
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        if not UtilClient.is_unset(request.union_id):
            query['UnionId'] = request.union_id
        body = {}
        if not UtilClient.is_unset(request.lang):
            body['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAttacks',
            version='2024-07-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            sas_rasp_20240727_models.DescribeAttacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_attacks(
        self,
        request: sas_rasp_20240727_models.DescribeAttacksRequest,
    ) -> sas_rasp_20240727_models.DescribeAttacksResponse:
        """
        @summary 查询攻击项
        
        @param request: DescribeAttacksRequest
        @return: DescribeAttacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_attacks_with_options(request, runtime)

    async def describe_attacks_async(
        self,
        request: sas_rasp_20240727_models.DescribeAttacksRequest,
    ) -> sas_rasp_20240727_models.DescribeAttacksResponse:
        """
        @summary 查询攻击项
        
        @param request: DescribeAttacksRequest
        @return: DescribeAttacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_attacks_with_options_async(request, runtime)
