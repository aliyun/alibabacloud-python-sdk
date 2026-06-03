# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_yundun_dbaudit20180320 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('yundun-dbaudit', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def config_instance_network_with_options(
        self,
        request: main_models.ConfigInstanceNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigInstanceNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.private_white_list):
            query['PrivateWhiteList'] = request.private_white_list
        if not DaraCore.is_null(request.public_access_control):
            query['PublicAccessControl'] = request.public_access_control
        if not DaraCore.is_null(request.public_white_list):
            query['PublicWhiteList'] = request.public_white_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigInstanceNetwork',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigInstanceNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_instance_network_with_options_async(
        self,
        request: main_models.ConfigInstanceNetworkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigInstanceNetworkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.private_white_list):
            query['PrivateWhiteList'] = request.private_white_list
        if not DaraCore.is_null(request.public_access_control):
            query['PublicAccessControl'] = request.public_access_control
        if not DaraCore.is_null(request.public_white_list):
            query['PublicWhiteList'] = request.public_white_list
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigInstanceNetwork',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigInstanceNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_instance_network(
        self,
        request: main_models.ConfigInstanceNetworkRequest,
    ) -> main_models.ConfigInstanceNetworkResponse:
        runtime = RuntimeOptions()
        return self.config_instance_network_with_options(request, runtime)

    async def config_instance_network_async(
        self,
        request: main_models.ConfigInstanceNetworkRequest,
    ) -> main_models.ConfigInstanceNetworkResponse:
        runtime = RuntimeOptions()
        return await self.config_instance_network_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: main_models.DescribeInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAttribute',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: main_models.DescribeInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAttribute',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: main_models.DescribeInstanceAttributeRequest,
    ) -> main_models.DescribeInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: main_models.DescribeInstanceAttributeRequest,
    ) -> main_models.DescribeInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_login_ticket_with_options(
        self,
        request: main_models.DescribeLoginTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoginTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoginTicket',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoginTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_login_ticket_with_options_async(
        self,
        request: main_models.DescribeLoginTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLoginTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLoginTicket',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLoginTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_login_ticket(
        self,
        request: main_models.DescribeLoginTicketRequest,
    ) -> main_models.DescribeLoginTicketResponse:
        runtime = RuntimeOptions()
        return self.describe_login_ticket_with_options(request, runtime)

    async def describe_login_ticket_async(
        self,
        request: main_models.DescribeLoginTicketRequest,
    ) -> main_models.DescribeLoginTicketResponse:
        runtime = RuntimeOptions()
        return await self.describe_login_ticket_with_options_async(request, runtime)

    def describe_sync_info_with_options(
        self,
        request: main_models.DescribeSyncInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyncInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyncInfo',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyncInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sync_info_with_options_async(
        self,
        request: main_models.DescribeSyncInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyncInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyncInfo',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyncInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sync_info(
        self,
        request: main_models.DescribeSyncInfoRequest,
    ) -> main_models.DescribeSyncInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_sync_info_with_options(request, runtime)

    async def describe_sync_info_async(
        self,
        request: main_models.DescribeSyncInfoRequest,
    ) -> main_models.DescribeSyncInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_sync_info_with_options_async(request, runtime)

    def get_agent_list_with_options(
        self,
        request: main_models.GetAgentListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_ip):
            query['AgentIp'] = request.agent_ip
        if not DaraCore.is_null(request.agent_os):
            query['AgentOs'] = request.agent_os
        if not DaraCore.is_null(request.agent_status):
            query['AgentStatus'] = request.agent_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentList',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_list_with_options_async(
        self,
        request: main_models.GetAgentListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_ip):
            query['AgentIp'] = request.agent_ip
        if not DaraCore.is_null(request.agent_os):
            query['AgentOs'] = request.agent_os
        if not DaraCore.is_null(request.agent_status):
            query['AgentStatus'] = request.agent_status
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentList',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_list(
        self,
        request: main_models.GetAgentListRequest,
    ) -> main_models.GetAgentListResponse:
        runtime = RuntimeOptions()
        return self.get_agent_list_with_options(request, runtime)

    async def get_agent_list_async(
        self,
        request: main_models.GetAgentListRequest,
    ) -> main_models.GetAgentListResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_list_with_options_async(request, runtime)

    def get_audit_count_with_options(
        self,
        request: main_models.GetAuditCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditCount',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audit_count_with_options_async(
        self,
        request: main_models.GetAuditCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditCount',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audit_count(
        self,
        request: main_models.GetAuditCountRequest,
    ) -> main_models.GetAuditCountResponse:
        runtime = RuntimeOptions()
        return self.get_audit_count_with_options(request, runtime)

    async def get_audit_count_async(
        self,
        request: main_models.GetAuditCountRequest,
    ) -> main_models.GetAuditCountResponse:
        runtime = RuntimeOptions()
        return await self.get_audit_count_with_options_async(request, runtime)

    def get_audit_count_distribution_with_options(
        self,
        request: main_models.GetAuditCountDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditCountDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditCountDistribution',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditCountDistributionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_audit_count_distribution_with_options_async(
        self,
        request: main_models.GetAuditCountDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuditCountDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAuditCountDistribution',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuditCountDistributionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_audit_count_distribution(
        self,
        request: main_models.GetAuditCountDistributionRequest,
    ) -> main_models.GetAuditCountDistributionResponse:
        runtime = RuntimeOptions()
        return self.get_audit_count_distribution_with_options(request, runtime)

    async def get_audit_count_distribution_async(
        self,
        request: main_models.GetAuditCountDistributionRequest,
    ) -> main_models.GetAuditCountDistributionResponse:
        runtime = RuntimeOptions()
        return await self.get_audit_count_distribution_with_options_async(request, runtime)

    def get_dbaudit_count_list_with_options(
        self,
        request: main_models.GetDBAuditCountListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDBAuditCountListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDBAuditCountList',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDBAuditCountListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dbaudit_count_list_with_options_async(
        self,
        request: main_models.GetDBAuditCountListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDBAuditCountListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDBAuditCountList',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDBAuditCountListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dbaudit_count_list(
        self,
        request: main_models.GetDBAuditCountListRequest,
    ) -> main_models.GetDBAuditCountListResponse:
        runtime = RuntimeOptions()
        return self.get_dbaudit_count_list_with_options(request, runtime)

    async def get_dbaudit_count_list_async(
        self,
        request: main_models.GetDBAuditCountListRequest,
    ) -> main_models.GetDBAuditCountListResponse:
        runtime = RuntimeOptions()
        return await self.get_dbaudit_count_list_with_options_async(request, runtime)

    def get_log_detail_with_options(
        self,
        request: main_models.GetLogDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogDetail',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_detail_with_options_async(
        self,
        request: main_models.GetLogDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogDetail',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_detail(
        self,
        request: main_models.GetLogDetailRequest,
    ) -> main_models.GetLogDetailResponse:
        runtime = RuntimeOptions()
        return self.get_log_detail_with_options(request, runtime)

    async def get_log_detail_async(
        self,
        request: main_models.GetLogDetailRequest,
    ) -> main_models.GetLogDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_log_detail_with_options_async(request, runtime)

    def get_log_list_with_options(
        self,
        request: main_models.GetLogListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.client_ip_list):
            query['ClientIpList'] = request.client_ip_list
        if not DaraCore.is_null(request.client_program_list):
            query['ClientProgramList'] = request.client_program_list
        if not DaraCore.is_null(request.db_host_list):
            query['DbHostList'] = request.db_host_list
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.db_user_list):
            query['DbUserList'] = request.db_user_list
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_success):
            query['IsSuccess'] = request.is_success
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_affect_rows):
            query['MaxAffectRows'] = request.max_affect_rows
        if not DaraCore.is_null(request.max_exec_cost_us):
            query['MaxExecCostUS'] = request.max_exec_cost_us
        if not DaraCore.is_null(request.min_affect_rows):
            query['MinAffectRows'] = request.min_affect_rows
        if not DaraCore.is_null(request.min_exec_cost_us):
            query['MinExecCostUS'] = request.min_exec_cost_us
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.risk_level_list):
            query['RiskLevelList'] = request.risk_level_list
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type_list):
            query['RuleTypeList'] = request.rule_type_list
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.sql_key):
            query['SqlKey'] = request.sql_key
        if not DaraCore.is_null(request.sql_type_list):
            query['SqlTypeList'] = request.sql_type_list
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogList',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_list_with_options_async(
        self,
        request: main_models.GetLogListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.client_ip_list):
            query['ClientIpList'] = request.client_ip_list
        if not DaraCore.is_null(request.client_program_list):
            query['ClientProgramList'] = request.client_program_list
        if not DaraCore.is_null(request.db_host_list):
            query['DbHostList'] = request.db_host_list
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.db_user_list):
            query['DbUserList'] = request.db_user_list
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.is_success):
            query['IsSuccess'] = request.is_success
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.max_affect_rows):
            query['MaxAffectRows'] = request.max_affect_rows
        if not DaraCore.is_null(request.max_exec_cost_us):
            query['MaxExecCostUS'] = request.max_exec_cost_us
        if not DaraCore.is_null(request.min_affect_rows):
            query['MinAffectRows'] = request.min_affect_rows
        if not DaraCore.is_null(request.min_exec_cost_us):
            query['MinExecCostUS'] = request.min_exec_cost_us
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.risk_level_list):
            query['RiskLevelList'] = request.risk_level_list
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.rule_type_list):
            query['RuleTypeList'] = request.rule_type_list
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sql_id):
            query['SqlId'] = request.sql_id
        if not DaraCore.is_null(request.sql_key):
            query['SqlKey'] = request.sql_key
        if not DaraCore.is_null(request.sql_type_list):
            query['SqlTypeList'] = request.sql_type_list
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogList',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_list(
        self,
        request: main_models.GetLogListRequest,
    ) -> main_models.GetLogListResponse:
        runtime = RuntimeOptions()
        return self.get_log_list_with_options(request, runtime)

    async def get_log_list_async(
        self,
        request: main_models.GetLogListRequest,
    ) -> main_models.GetLogListResponse:
        runtime = RuntimeOptions()
        return await self.get_log_list_with_options_async(request, runtime)

    def get_log_type_distribution_with_options(
        self,
        request: main_models.GetLogTypeDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogTypeDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogTypeDistribution',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogTypeDistributionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_type_distribution_with_options_async(
        self,
        request: main_models.GetLogTypeDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogTypeDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogTypeDistribution',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogTypeDistributionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_type_distribution(
        self,
        request: main_models.GetLogTypeDistributionRequest,
    ) -> main_models.GetLogTypeDistributionResponse:
        runtime = RuntimeOptions()
        return self.get_log_type_distribution_with_options(request, runtime)

    async def get_log_type_distribution_async(
        self,
        request: main_models.GetLogTypeDistributionRequest,
    ) -> main_models.GetLogTypeDistributionResponse:
        runtime = RuntimeOptions()
        return await self.get_log_type_distribution_with_options_async(request, runtime)

    def get_risk_level_distribution_with_options(
        self,
        request: main_models.GetRiskLevelDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRiskLevelDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRiskLevelDistribution',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRiskLevelDistributionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_risk_level_distribution_with_options_async(
        self,
        request: main_models.GetRiskLevelDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRiskLevelDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRiskLevelDistribution',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRiskLevelDistributionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_risk_level_distribution(
        self,
        request: main_models.GetRiskLevelDistributionRequest,
    ) -> main_models.GetRiskLevelDistributionResponse:
        runtime = RuntimeOptions()
        return self.get_risk_level_distribution_with_options(request, runtime)

    async def get_risk_level_distribution_async(
        self,
        request: main_models.GetRiskLevelDistributionRequest,
    ) -> main_models.GetRiskLevelDistributionResponse:
        runtime = RuntimeOptions()
        return await self.get_risk_level_distribution_with_options_async(request, runtime)

    def get_session_distribution_with_options(
        self,
        request: main_models.GetSessionDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSessionDistribution',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSessionDistributionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_session_distribution_with_options_async(
        self,
        request: main_models.GetSessionDistributionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionDistributionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSessionDistribution',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSessionDistributionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_session_distribution(
        self,
        request: main_models.GetSessionDistributionRequest,
    ) -> main_models.GetSessionDistributionResponse:
        runtime = RuntimeOptions()
        return self.get_session_distribution_with_options(request, runtime)

    async def get_session_distribution_async(
        self,
        request: main_models.GetSessionDistributionRequest,
    ) -> main_models.GetSessionDistributionResponse:
        runtime = RuntimeOptions()
        return await self.get_session_distribution_with_options_async(request, runtime)

    def get_session_list_with_options(
        self,
        request: main_models.GetSessionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_list):
            query['ActionList'] = request.action_list
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.client_ip_list):
            query['ClientIpList'] = request.client_ip_list
        if not DaraCore.is_null(request.client_program_list):
            query['ClientProgramList'] = request.client_program_list
        if not DaraCore.is_null(request.db_host_list):
            query['DbHostList'] = request.db_host_list
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.db_user_list):
            query['DbUserList'] = request.db_user_list
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSessionList',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSessionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_session_list_with_options_async(
        self,
        request: main_models.GetSessionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSessionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_list):
            query['ActionList'] = request.action_list
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.client_ip_list):
            query['ClientIpList'] = request.client_ip_list
        if not DaraCore.is_null(request.client_program_list):
            query['ClientProgramList'] = request.client_program_list
        if not DaraCore.is_null(request.db_host_list):
            query['DbHostList'] = request.db_host_list
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.db_user_list):
            query['DbUserList'] = request.db_user_list
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSessionList',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSessionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_session_list(
        self,
        request: main_models.GetSessionListRequest,
    ) -> main_models.GetSessionListResponse:
        runtime = RuntimeOptions()
        return self.get_session_list_with_options(request, runtime)

    async def get_session_list_async(
        self,
        request: main_models.GetSessionListRequest,
    ) -> main_models.GetSessionListResponse:
        runtime = RuntimeOptions()
        return await self.get_session_list_with_options_async(request, runtime)

    def list_data_source_attribute_with_options(
        self,
        request: main_models.ListDataSourceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_ids):
            query['DbIds'] = request.db_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceAttribute',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_attribute_with_options_async(
        self,
        request: main_models.ListDataSourceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_ids):
            query['DbIds'] = request.db_ids
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceAttribute',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_attribute(
        self,
        request: main_models.ListDataSourceAttributeRequest,
    ) -> main_models.ListDataSourceAttributeResponse:
        runtime = RuntimeOptions()
        return self.list_data_source_attribute_with_options(request, runtime)

    async def list_data_source_attribute_async(
        self,
        request: main_models.ListDataSourceAttributeRequest,
    ) -> main_models.ListDataSourceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.list_data_source_attribute_with_options_async(request, runtime)

    def list_data_sources_with_options(
        self,
        request: main_models.ListDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSources',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        request: main_models.ListDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_id):
            query['DbId'] = request.db_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSources',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sources(
        self,
        request: main_models.ListDataSourcesRequest,
    ) -> main_models.ListDataSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    async def list_data_sources_async(
        self,
        request: main_models.ListDataSourcesRequest,
    ) -> main_models.ListDataSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_sources_with_options_async(request, runtime)

    def list_system_alarms_with_options(
        self,
        request: main_models.ListSystemAlarmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemAlarmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemAlarms',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_alarms_with_options_async(
        self,
        request: main_models.ListSystemAlarmsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSystemAlarmsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not DaraCore.is_null(request.begin_date):
            query['BeginDate'] = request.begin_date
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSystemAlarms',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSystemAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_alarms(
        self,
        request: main_models.ListSystemAlarmsRequest,
    ) -> main_models.ListSystemAlarmsResponse:
        runtime = RuntimeOptions()
        return self.list_system_alarms_with_options(request, runtime)

    async def list_system_alarms_async(
        self,
        request: main_models.ListSystemAlarmsRequest,
    ) -> main_models.ListSystemAlarmsResponse:
        runtime = RuntimeOptions()
        return await self.list_system_alarms_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceAttribute',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceAttribute',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
    ) -> main_models.ModifyInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: main_models.ModifyInstanceAttributeRequest,
    ) -> main_models.ModifyInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: main_models.StartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: main_models.StartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartInstance',
            version = '2018-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        request: main_models.StartInstanceRequest,
    ) -> main_models.StartInstanceResponse:
        runtime = RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: main_models.StartInstanceRequest,
    ) -> main_models.StartInstanceResponse:
        runtime = RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)
