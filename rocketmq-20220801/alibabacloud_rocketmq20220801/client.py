# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_rocketmq20220801 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('rocketmq', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_disaster_recovery_item_with_options(
        self,
        plan_id: str,
        request: main_models.AddDisasterRecoveryItemRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDisasterRecoveryItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.topics):
            body['topics'] = request.topics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDisasterRecoveryItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_disaster_recovery_item_with_options_async(
        self,
        plan_id: str,
        request: main_models.AddDisasterRecoveryItemRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDisasterRecoveryItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.topics):
            body['topics'] = request.topics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDisasterRecoveryItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_disaster_recovery_item(
        self,
        plan_id: str,
        request: main_models.AddDisasterRecoveryItemRequest,
    ) -> main_models.AddDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_disaster_recovery_item_with_options(plan_id, request, headers, runtime)

    async def add_disaster_recovery_item_async(
        self,
        plan_id: str,
        request: main_models.AddDisasterRecoveryItemRequest,
    ) -> main_models.AddDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_disaster_recovery_item_with_options_async(plan_id, request, headers, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/resourceGroup/change',
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
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/resourceGroup/change',
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

    def create_consumer_group_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.consume_retry_policy):
            body['consumeRetryPolicy'] = request.consume_retry_policy
        if not DaraCore.is_null(request.delivery_order_type):
            body['deliveryOrderType'] = request.delivery_order_type
        if not DaraCore.is_null(request.max_receive_tps):
            body['maxReceiveTps'] = request.max_receive_tps
        if not DaraCore.is_null(request.message_model):
            body['messageModel'] = request.message_model
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        if not DaraCore.is_null(request.topic_name):
            body['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerGroup',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}',
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
        instance_id: str,
        consumer_group_id: str,
        request: main_models.CreateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateConsumerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.consume_retry_policy):
            body['consumeRetryPolicy'] = request.consume_retry_policy
        if not DaraCore.is_null(request.delivery_order_type):
            body['deliveryOrderType'] = request.delivery_order_type
        if not DaraCore.is_null(request.max_receive_tps):
            body['maxReceiveTps'] = request.max_receive_tps
        if not DaraCore.is_null(request.message_model):
            body['messageModel'] = request.message_model
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        if not DaraCore.is_null(request.topic_name):
            body['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConsumerGroup',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}',
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
        instance_id: str,
        consumer_group_id: str,
        request: main_models.CreateConsumerGroupRequest,
    ) -> main_models.CreateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_consumer_group_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def create_consumer_group_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.CreateConsumerGroupRequest,
    ) -> main_models.CreateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_consumer_group_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def create_disaster_recovery_plan_with_options(
        self,
        request: main_models.CreateDisasterRecoveryPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDisasterRecoveryPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_sync_checkpoint):
            body['autoSyncCheckpoint'] = request.auto_sync_checkpoint
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.plan_desc):
            body['planDesc'] = request.plan_desc
        if not DaraCore.is_null(request.plan_name):
            body['planName'] = request.plan_name
        if not DaraCore.is_null(request.plan_type):
            body['planType'] = request.plan_type
        if not DaraCore.is_null(request.sync_checkpoint_enabled):
            body['syncCheckpointEnabled'] = request.sync_checkpoint_enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDisasterRecoveryPlan',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDisasterRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_disaster_recovery_plan_with_options_async(
        self,
        request: main_models.CreateDisasterRecoveryPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDisasterRecoveryPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_sync_checkpoint):
            body['autoSyncCheckpoint'] = request.auto_sync_checkpoint
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.plan_desc):
            body['planDesc'] = request.plan_desc
        if not DaraCore.is_null(request.plan_name):
            body['planName'] = request.plan_name
        if not DaraCore.is_null(request.plan_type):
            body['planType'] = request.plan_type
        if not DaraCore.is_null(request.sync_checkpoint_enabled):
            body['syncCheckpointEnabled'] = request.sync_checkpoint_enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDisasterRecoveryPlan',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDisasterRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_disaster_recovery_plan(
        self,
        request: main_models.CreateDisasterRecoveryPlanRequest,
    ) -> main_models.CreateDisasterRecoveryPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_disaster_recovery_plan_with_options(request, headers, runtime)

    async def create_disaster_recovery_plan_async(
        self,
        request: main_models.CreateDisasterRecoveryPlanRequest,
    ) -> main_models.CreateDisasterRecoveryPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_disaster_recovery_plan_with_options_async(request, headers, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            body['autoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.commodity_code):
            body['commodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.network_info):
            body['networkInfo'] = request.network_info
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.period):
            body['period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['periodUnit'] = request.period_unit
        if not DaraCore.is_null(request.product_info):
            body['productInfo'] = request.product_info
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.series_code):
            body['seriesCode'] = request.series_code
        if not DaraCore.is_null(request.service_code):
            body['serviceCode'] = request.service_code
        if not DaraCore.is_null(request.sub_series_code):
            body['subSeriesCode'] = request.sub_series_code
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.auto_renew_period):
            body['autoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.commodity_code):
            body['commodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.network_info):
            body['networkInfo'] = request.network_info
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.period):
            body['period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            body['periodUnit'] = request.period_unit
        if not DaraCore.is_null(request.product_info):
            body['productInfo'] = request.product_info
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.series_code):
            body['seriesCode'] = request.series_code
        if not DaraCore.is_null(request.service_code):
            body['serviceCode'] = request.service_code
        if not DaraCore.is_null(request.sub_series_code):
            body['subSeriesCode'] = request.sub_series_code
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_instance_account_with_options(
        self,
        instance_id: str,
        request: main_models.CreateInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        if not DaraCore.is_null(request.username):
            body['username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceAccount',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/accounts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_account_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceAccountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.password):
            body['password'] = request.password
        if not DaraCore.is_null(request.username):
            body['username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceAccount',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/accounts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_account(
        self,
        instance_id: str,
        request: main_models.CreateInstanceAccountRequest,
    ) -> main_models.CreateInstanceAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_account_with_options(instance_id, request, headers, runtime)

    async def create_instance_account_async(
        self,
        instance_id: str,
        request: main_models.CreateInstanceAccountRequest,
    ) -> main_models.CreateInstanceAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_account_with_options_async(instance_id, request, headers, runtime)

    def create_instance_acl_with_options(
        self,
        instance_id: str,
        username: str,
        request: main_models.CreateInstanceAclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceAclResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.actions):
            body['actions'] = request.actions
        if not DaraCore.is_null(request.decision):
            body['decision'] = request.decision
        if not DaraCore.is_null(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        if not DaraCore.is_null(request.resource_name):
            body['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceAcl',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/acl/account/{DaraURL.percent_encode(username)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_acl_with_options_async(
        self,
        instance_id: str,
        username: str,
        request: main_models.CreateInstanceAclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceAclResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.actions):
            body['actions'] = request.actions
        if not DaraCore.is_null(request.decision):
            body['decision'] = request.decision
        if not DaraCore.is_null(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        if not DaraCore.is_null(request.resource_name):
            body['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceAcl',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/acl/account/{DaraURL.percent_encode(username)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_acl(
        self,
        instance_id: str,
        username: str,
        request: main_models.CreateInstanceAclRequest,
    ) -> main_models.CreateInstanceAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_acl_with_options(instance_id, username, request, headers, runtime)

    async def create_instance_acl_async(
        self,
        instance_id: str,
        username: str,
        request: main_models.CreateInstanceAclRequest,
    ) -> main_models.CreateInstanceAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_acl_with_options_async(instance_id, username, request, headers, runtime)

    def create_instance_ip_whitelist_with_options(
        self,
        instance_id: str,
        request: main_models.CreateInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceIpWhitelistResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceIpWhitelist',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/ip/whitelist',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_ip_whitelist_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceIpWhitelistResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceIpWhitelist',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/ip/whitelist',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_ip_whitelist(
        self,
        instance_id: str,
        request: main_models.CreateInstanceIpWhitelistRequest,
    ) -> main_models.CreateInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_ip_whitelist_with_options(instance_id, request, headers, runtime)

    async def create_instance_ip_whitelist_async(
        self,
        instance_id: str,
        request: main_models.CreateInstanceIpWhitelistRequest,
    ) -> main_models.CreateInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_ip_whitelist_with_options_async(instance_id, request, headers, runtime)

    def create_topic_with_options(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.CreateTopicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTopicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lite_topic_expiration):
            body['liteTopicExpiration'] = request.lite_topic_expiration
        if not DaraCore.is_null(request.max_send_tps):
            body['maxSendTps'] = request.max_send_tps
        if not DaraCore.is_null(request.message_type):
            body['messageType'] = request.message_type
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTopic',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_topic_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.CreateTopicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTopicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lite_topic_expiration):
            body['liteTopicExpiration'] = request.lite_topic_expiration
        if not DaraCore.is_null(request.max_send_tps):
            body['maxSendTps'] = request.max_send_tps
        if not DaraCore.is_null(request.message_type):
            body['messageType'] = request.message_type
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTopic',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_topic(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.CreateTopicRequest,
    ) -> main_models.CreateTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_topic_with_options(instance_id, topic_name, request, headers, runtime)

    async def create_topic_async(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.CreateTopicRequest,
    ) -> main_models.CreateTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_topic_with_options_async(instance_id, topic_name, request, headers, runtime)

    def delete_consumer_group_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroup',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}',
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
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroup',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}',
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
        instance_id: str,
        consumer_group_id: str,
    ) -> main_models.DeleteConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_with_options(instance_id, consumer_group_id, headers, runtime)

    async def delete_consumer_group_async(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> main_models.DeleteConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_consumer_group_with_options_async(instance_id, consumer_group_id, headers, runtime)

    def delete_consumer_group_subscription_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.DeleteConsumerGroupSubscriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_expression):
            query['filterExpression'] = request.filter_expression
        if not DaraCore.is_null(request.filter_type):
            query['filterType'] = request.filter_type
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroupSubscription',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/subscriptions',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerGroupSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_group_subscription_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.DeleteConsumerGroupSubscriptionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConsumerGroupSubscriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_expression):
            query['filterExpression'] = request.filter_expression
        if not DaraCore.is_null(request.filter_type):
            query['filterType'] = request.filter_type
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConsumerGroupSubscription',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/subscriptions',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConsumerGroupSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_group_subscription(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.DeleteConsumerGroupSubscriptionRequest,
    ) -> main_models.DeleteConsumerGroupSubscriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_consumer_group_subscription_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def delete_consumer_group_subscription_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.DeleteConsumerGroupSubscriptionRequest,
    ) -> main_models.DeleteConsumerGroupSubscriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_consumer_group_subscription_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def delete_disaster_recovery_item_with_options(
        self,
        plan_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDisasterRecoveryItemResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDisasterRecoveryItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_disaster_recovery_item_with_options_async(
        self,
        plan_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDisasterRecoveryItemResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDisasterRecoveryItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_disaster_recovery_item(
        self,
        plan_id: str,
        item_id: str,
    ) -> main_models.DeleteDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_disaster_recovery_item_with_options(plan_id, item_id, headers, runtime)

    async def delete_disaster_recovery_item_async(
        self,
        plan_id: str,
        item_id: str,
    ) -> main_models.DeleteDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_disaster_recovery_item_with_options_async(plan_id, item_id, headers, runtime)

    def delete_disaster_recovery_plan_with_options(
        self,
        plan_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDisasterRecoveryPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDisasterRecoveryPlan',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDisasterRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_disaster_recovery_plan_with_options_async(
        self,
        plan_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDisasterRecoveryPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteDisasterRecoveryPlan',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDisasterRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_disaster_recovery_plan(
        self,
        plan_id: str,
    ) -> main_models.DeleteDisasterRecoveryPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_disaster_recovery_plan_with_options(plan_id, headers, runtime)

    async def delete_disaster_recovery_plan_async(
        self,
        plan_id: str,
    ) -> main_models.DeleteDisasterRecoveryPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_disaster_recovery_plan_with_options_async(plan_id, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, headers, runtime)

    def delete_instance_account_with_options(
        self,
        instance_id: str,
        username: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceAccountResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceAccount',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/accounts/{DaraURL.percent_encode(username)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_account_with_options_async(
        self,
        instance_id: str,
        username: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceAccountResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceAccount',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/accounts/{DaraURL.percent_encode(username)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_account(
        self,
        instance_id: str,
        username: str,
    ) -> main_models.DeleteInstanceAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_account_with_options(instance_id, username, headers, runtime)

    async def delete_instance_account_async(
        self,
        instance_id: str,
        username: str,
    ) -> main_models.DeleteInstanceAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_account_with_options_async(instance_id, username, headers, runtime)

    def delete_instance_acl_with_options(
        self,
        instance_id: str,
        username: str,
        request: main_models.DeleteInstanceAclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_name):
            query['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceAcl',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/acl/account/{DaraURL.percent_encode(username)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_acl_with_options_async(
        self,
        instance_id: str,
        username: str,
        request: main_models.DeleteInstanceAclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_name):
            query['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceAcl',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/acl/account/{DaraURL.percent_encode(username)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_acl(
        self,
        instance_id: str,
        username: str,
        request: main_models.DeleteInstanceAclRequest,
    ) -> main_models.DeleteInstanceAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_acl_with_options(instance_id, username, request, headers, runtime)

    async def delete_instance_acl_async(
        self,
        instance_id: str,
        username: str,
        request: main_models.DeleteInstanceAclRequest,
    ) -> main_models.DeleteInstanceAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_acl_with_options_async(instance_id, username, request, headers, runtime)

    def delete_instance_ip_whitelist_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.DeleteInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceIpWhitelistResponse:
        tmp_req.validate()
        request = main_models.DeleteInstanceIpWhitelistShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_whitelists):
            request.ip_whitelists_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_whitelists, 'ipWhitelists', 'simple')
        query = {}
        if not DaraCore.is_null(request.ip_whitelist):
            query['ipWhitelist'] = request.ip_whitelist
        if not DaraCore.is_null(request.ip_whitelists_shrink):
            query['ipWhitelists'] = request.ip_whitelists_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceIpWhitelist',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/ip/whitelist',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_ip_whitelist_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.DeleteInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceIpWhitelistResponse:
        tmp_req.validate()
        request = main_models.DeleteInstanceIpWhitelistShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_whitelists):
            request.ip_whitelists_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_whitelists, 'ipWhitelists', 'simple')
        query = {}
        if not DaraCore.is_null(request.ip_whitelist):
            query['ipWhitelist'] = request.ip_whitelist
        if not DaraCore.is_null(request.ip_whitelists_shrink):
            query['ipWhitelists'] = request.ip_whitelists_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceIpWhitelist',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/ip/whitelist',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_ip_whitelist(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceIpWhitelistRequest,
    ) -> main_models.DeleteInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_ip_whitelist_with_options(instance_id, request, headers, runtime)

    async def delete_instance_ip_whitelist_async(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceIpWhitelistRequest,
    ) -> main_models.DeleteInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_ip_whitelist_with_options_async(instance_id, request, headers, runtime)

    def delete_topic_with_options(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTopicResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTopic',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_topic_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTopicResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTopic',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_topic(
        self,
        instance_id: str,
        topic_name: str,
    ) -> main_models.DeleteTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_topic_with_options(instance_id, topic_name, headers, runtime)

    async def delete_topic_async(
        self,
        instance_id: str,
        topic_name: str,
    ) -> main_models.DeleteTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_topic_with_options_async(instance_id, topic_name, headers, runtime)

    def execute_migration_operation_with_options(
        self,
        migration_id: str,
        stage_type: str,
        operation_id: str,
        request: main_models.ExecuteMigrationOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteMigrationOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.operation_param):
            body['operationParam'] = request.operation_param
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteMigrationOperation',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/migrations/{DaraURL.percent_encode(migration_id)}/stages/{DaraURL.percent_encode(stage_type)}/operations/{DaraURL.percent_encode(operation_id)}/execute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteMigrationOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_migration_operation_with_options_async(
        self,
        migration_id: str,
        stage_type: str,
        operation_id: str,
        request: main_models.ExecuteMigrationOperationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteMigrationOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        body = {}
        if not DaraCore.is_null(request.operation_param):
            body['operationParam'] = request.operation_param
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteMigrationOperation',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/migrations/{DaraURL.percent_encode(migration_id)}/stages/{DaraURL.percent_encode(stage_type)}/operations/{DaraURL.percent_encode(operation_id)}/execute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteMigrationOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_migration_operation(
        self,
        migration_id: str,
        stage_type: str,
        operation_id: str,
        request: main_models.ExecuteMigrationOperationRequest,
    ) -> main_models.ExecuteMigrationOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_migration_operation_with_options(migration_id, stage_type, operation_id, request, headers, runtime)

    async def execute_migration_operation_async(
        self,
        migration_id: str,
        stage_type: str,
        operation_id: str,
        request: main_models.ExecuteMigrationOperationRequest,
    ) -> main_models.ExecuteMigrationOperationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_migration_operation_with_options_async(migration_id, stage_type, operation_id, request, headers, runtime)

    def finish_migration_stage_with_options(
        self,
        migration_id: str,
        stage_type: str,
        request: main_models.FinishMigrationStageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FinishMigrationStageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FinishMigrationStage',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/migrations/{DaraURL.percent_encode(migration_id)}/stages/{DaraURL.percent_encode(stage_type)}/finish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishMigrationStageResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_migration_stage_with_options_async(
        self,
        migration_id: str,
        stage_type: str,
        request: main_models.FinishMigrationStageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FinishMigrationStageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FinishMigrationStage',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/migrations/{DaraURL.percent_encode(migration_id)}/stages/{DaraURL.percent_encode(stage_type)}/finish',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishMigrationStageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_migration_stage(
        self,
        migration_id: str,
        stage_type: str,
        request: main_models.FinishMigrationStageRequest,
    ) -> main_models.FinishMigrationStageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.finish_migration_stage_with_options(migration_id, stage_type, request, headers, runtime)

    async def finish_migration_stage_async(
        self,
        migration_id: str,
        stage_type: str,
        request: main_models.FinishMigrationStageRequest,
    ) -> main_models.FinishMigrationStageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.finish_migration_stage_with_options_async(migration_id, stage_type, request, headers, runtime)

    def get_consume_timespan_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumeTimespanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumeTimespan',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/consumeTimespan/{DaraURL.percent_encode(topic_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumeTimespanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consume_timespan_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumeTimespanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumeTimespan',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/consumeTimespan/{DaraURL.percent_encode(topic_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumeTimespanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consume_timespan(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
    ) -> main_models.GetConsumeTimespanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consume_timespan_with_options(instance_id, consumer_group_id, topic_name, headers, runtime)

    async def get_consume_timespan_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
    ) -> main_models.GetConsumeTimespanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consume_timespan_with_options_async(instance_id, consumer_group_id, topic_name, headers, runtime)

    def get_consumer_group_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerGroup',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}',
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
        instance_id: str,
        consumer_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerGroup',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}',
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
        instance_id: str,
        consumer_group_id: str,
    ) -> main_models.GetConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consumer_group_with_options(instance_id, consumer_group_id, headers, runtime)

    async def get_consumer_group_async(
        self,
        instance_id: str,
        consumer_group_id: str,
    ) -> main_models.GetConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consumer_group_with_options_async(instance_id, consumer_group_id, headers, runtime)

    def get_consumer_group_lag_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.GetConsumerGroupLagRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerGroupLagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lite_topic_name):
            query['liteTopicName'] = request.lite_topic_name
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerGroupLag',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/lag',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerGroupLagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_group_lag_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.GetConsumerGroupLagRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerGroupLagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lite_topic_name):
            query['liteTopicName'] = request.lite_topic_name
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerGroupLag',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/lag',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerGroupLagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_group_lag(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.GetConsumerGroupLagRequest,
    ) -> main_models.GetConsumerGroupLagResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consumer_group_lag_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def get_consumer_group_lag_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.GetConsumerGroupLagRequest,
    ) -> main_models.GetConsumerGroupLagResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consumer_group_lag_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def get_consumer_group_subscription_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerGroupSubscriptionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerGroupSubscription',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/subscriptions/{DaraURL.percent_encode(topic_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerGroupSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_group_subscription_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerGroupSubscriptionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerGroupSubscription',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/subscriptions/{DaraURL.percent_encode(topic_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerGroupSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_group_subscription(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
    ) -> main_models.GetConsumerGroupSubscriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consumer_group_subscription_with_options(instance_id, consumer_group_id, topic_name, headers, runtime)

    async def get_consumer_group_subscription_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
    ) -> main_models.GetConsumerGroupSubscriptionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consumer_group_subscription_with_options_async(instance_id, consumer_group_id, topic_name, headers, runtime)

    def get_consumer_stack_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.GetConsumerStackRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerStack',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/stack',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consumer_stack_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.GetConsumerStackRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetConsumerStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsumerStack',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/stack',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsumerStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consumer_stack(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.GetConsumerStackRequest,
    ) -> main_models.GetConsumerStackResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_consumer_stack_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def get_consumer_stack_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.GetConsumerStackRequest,
    ) -> main_models.GetConsumerStackResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_consumer_stack_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def get_disaster_recovery_item_with_options(
        self,
        plan_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDisasterRecoveryItemResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDisasterRecoveryItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_disaster_recovery_item_with_options_async(
        self,
        plan_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDisasterRecoveryItemResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDisasterRecoveryItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_disaster_recovery_item(
        self,
        plan_id: str,
        item_id: str,
    ) -> main_models.GetDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_disaster_recovery_item_with_options(plan_id, item_id, headers, runtime)

    async def get_disaster_recovery_item_async(
        self,
        plan_id: str,
        item_id: str,
    ) -> main_models.GetDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_disaster_recovery_item_with_options_async(plan_id, item_id, headers, runtime)

    def get_disaster_recovery_plan_with_options(
        self,
        plan_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDisasterRecoveryPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDisasterRecoveryPlan',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDisasterRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_disaster_recovery_plan_with_options_async(
        self,
        plan_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDisasterRecoveryPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDisasterRecoveryPlan',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDisasterRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_disaster_recovery_plan(
        self,
        plan_id: str,
    ) -> main_models.GetDisasterRecoveryPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_disaster_recovery_plan_with_options(plan_id, headers, runtime)

    async def get_disaster_recovery_plan_async(
        self,
        plan_id: str,
    ) -> main_models.GetDisasterRecoveryPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_disaster_recovery_plan_with_options_async(plan_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_instance_account_with_options(
        self,
        instance_id: str,
        request: main_models.GetInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.username):
            query['username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceAccount',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/account',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_account_with_options_async(
        self,
        instance_id: str,
        request: main_models.GetInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.username):
            query['username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceAccount',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/account',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_account(
        self,
        instance_id: str,
        request: main_models.GetInstanceAccountRequest,
    ) -> main_models.GetInstanceAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_account_with_options(instance_id, request, headers, runtime)

    async def get_instance_account_async(
        self,
        instance_id: str,
        request: main_models.GetInstanceAccountRequest,
    ) -> main_models.GetInstanceAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_account_with_options_async(instance_id, request, headers, runtime)

    def get_instance_acl_with_options(
        self,
        instance_id: str,
        username: str,
        request: main_models.GetInstanceAclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_name):
            query['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceAcl',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/acl/account/{DaraURL.percent_encode(username)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_acl_with_options_async(
        self,
        instance_id: str,
        username: str,
        request: main_models.GetInstanceAclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_name):
            query['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceAcl',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/acl/account/{DaraURL.percent_encode(username)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_acl(
        self,
        instance_id: str,
        username: str,
        request: main_models.GetInstanceAclRequest,
    ) -> main_models.GetInstanceAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_acl_with_options(instance_id, username, request, headers, runtime)

    async def get_instance_acl_async(
        self,
        instance_id: str,
        username: str,
        request: main_models.GetInstanceAclRequest,
    ) -> main_models.GetInstanceAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_acl_with_options_async(instance_id, username, request, headers, runtime)

    def get_instance_ip_whitelist_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.GetInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceIpWhitelistResponse:
        tmp_req.validate()
        request = main_models.GetInstanceIpWhitelistShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_whitelists):
            request.ip_whitelists_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_whitelists, 'ipWhitelists', 'simple')
        query = {}
        if not DaraCore.is_null(request.ip_whitelists_shrink):
            query['ipWhitelists'] = request.ip_whitelists_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceIpWhitelist',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/ip/whitelists',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_ip_whitelist_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.GetInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceIpWhitelistResponse:
        tmp_req.validate()
        request = main_models.GetInstanceIpWhitelistShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_whitelists):
            request.ip_whitelists_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_whitelists, 'ipWhitelists', 'simple')
        query = {}
        if not DaraCore.is_null(request.ip_whitelists_shrink):
            query['ipWhitelists'] = request.ip_whitelists_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceIpWhitelist',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/ip/whitelists',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_ip_whitelist(
        self,
        instance_id: str,
        request: main_models.GetInstanceIpWhitelistRequest,
    ) -> main_models.GetInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_ip_whitelist_with_options(instance_id, request, headers, runtime)

    async def get_instance_ip_whitelist_async(
        self,
        instance_id: str,
        request: main_models.GetInstanceIpWhitelistRequest,
    ) -> main_models.GetInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_ip_whitelist_with_options_async(instance_id, request, headers, runtime)

    def get_message_detail_with_options(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageDetailResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMessageDetail',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/messages/{DaraURL.percent_encode(message_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_message_detail_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMessageDetailResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMessageDetail',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/messages/{DaraURL.percent_encode(message_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMessageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_message_detail(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
    ) -> main_models.GetMessageDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_message_detail_with_options(instance_id, topic_name, message_id, headers, runtime)

    async def get_message_detail_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
    ) -> main_models.GetMessageDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_message_detail_with_options_async(instance_id, topic_name, message_id, headers, runtime)

    def get_topic_with_options(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTopic',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTopic',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic(
        self,
        instance_id: str,
        topic_name: str,
    ) -> main_models.GetTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_topic_with_options(instance_id, topic_name, headers, runtime)

    async def get_topic_async(
        self,
        instance_id: str,
        topic_name: str,
    ) -> main_models.GetTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_topic_with_options_async(instance_id, topic_name, headers, runtime)

    def get_trace_with_options(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: main_models.GetTraceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrace',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/traces/{DaraURL.percent_encode(message_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: main_models.GetTraceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrace',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/traces/{DaraURL.percent_encode(message_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: main_models.GetTraceRequest,
    ) -> main_models.GetTraceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_trace_with_options(instance_id, topic_name, message_id, request, headers, runtime)

    async def get_trace_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: main_models.GetTraceRequest,
    ) -> main_models.GetTraceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_trace_with_options_async(instance_id, topic_name, message_id, request, headers, runtime)

    def list_available_zones_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableZonesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableZones',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/zones',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_zones_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAvailableZonesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListAvailableZones',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/zones',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvailableZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_zones(self) -> main_models.ListAvailableZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_available_zones_with_options(headers, runtime)

    async def list_available_zones_async(self) -> main_models.ListAvailableZonesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_available_zones_with_options_async(headers, runtime)

    def list_consumer_connections_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.ListConsumerConnectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lite_topic_name):
            query['liteTopicName'] = request.lite_topic_name
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerConnections',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/connections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerConnectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumer_connections_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.ListConsumerConnectionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerConnectionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lite_topic_name):
            query['liteTopicName'] = request.lite_topic_name
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerConnections',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/connections',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerConnectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumer_connections(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.ListConsumerConnectionsRequest,
    ) -> main_models.ListConsumerConnectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumer_connections_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def list_consumer_connections_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.ListConsumerConnectionsRequest,
    ) -> main_models.ListConsumerConnectionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumer_connections_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def list_consumer_group_subscriptions_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupSubscriptionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupSubscriptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerGroupSubscriptions',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/subscriptions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerGroupSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_consumer_group_subscriptions_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupSubscriptionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupSubscriptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConsumerGroupSubscriptions',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/subscriptions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConsumerGroupSubscriptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_consumer_group_subscriptions(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupSubscriptionsRequest,
    ) -> main_models.ListConsumerGroupSubscriptionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumer_group_subscriptions_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def list_consumer_group_subscriptions_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.ListConsumerGroupSubscriptionsRequest,
    ) -> main_models.ListConsumerGroupSubscriptionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumer_group_subscriptions_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def list_consumer_groups_with_options(
        self,
        instance_id: str,
        request: main_models.ListConsumerGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
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
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups',
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
        instance_id: str,
        request: main_models.ListConsumerGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListConsumerGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
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
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups',
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
        instance_id: str,
        request: main_models.ListConsumerGroupsRequest,
    ) -> main_models.ListConsumerGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_consumer_groups_with_options(instance_id, request, headers, runtime)

    async def list_consumer_groups_async(
        self,
        instance_id: str,
        request: main_models.ListConsumerGroupsRequest,
    ) -> main_models.ListConsumerGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_consumer_groups_with_options_async(instance_id, request, headers, runtime)

    def list_disaster_recovery_checkpoints_with_options(
        self,
        plan_id: str,
        item_id: str,
        request: main_models.ListDisasterRecoveryCheckpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDisasterRecoveryCheckpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDisasterRecoveryCheckpoints',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}/checkpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDisasterRecoveryCheckpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_disaster_recovery_checkpoints_with_options_async(
        self,
        plan_id: str,
        item_id: str,
        request: main_models.ListDisasterRecoveryCheckpointsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDisasterRecoveryCheckpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDisasterRecoveryCheckpoints',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}/checkpoints',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDisasterRecoveryCheckpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_disaster_recovery_checkpoints(
        self,
        plan_id: str,
        item_id: str,
        request: main_models.ListDisasterRecoveryCheckpointsRequest,
    ) -> main_models.ListDisasterRecoveryCheckpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_disaster_recovery_checkpoints_with_options(plan_id, item_id, request, headers, runtime)

    async def list_disaster_recovery_checkpoints_async(
        self,
        plan_id: str,
        item_id: str,
        request: main_models.ListDisasterRecoveryCheckpointsRequest,
    ) -> main_models.ListDisasterRecoveryCheckpointsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_disaster_recovery_checkpoints_with_options_async(plan_id, item_id, request, headers, runtime)

    def list_disaster_recovery_items_with_options(
        self,
        plan_id: str,
        request: main_models.ListDisasterRecoveryItemsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDisasterRecoveryItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDisasterRecoveryItems',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDisasterRecoveryItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_disaster_recovery_items_with_options_async(
        self,
        plan_id: str,
        request: main_models.ListDisasterRecoveryItemsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDisasterRecoveryItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDisasterRecoveryItems',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDisasterRecoveryItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_disaster_recovery_items(
        self,
        plan_id: str,
        request: main_models.ListDisasterRecoveryItemsRequest,
    ) -> main_models.ListDisasterRecoveryItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_disaster_recovery_items_with_options(plan_id, request, headers, runtime)

    async def list_disaster_recovery_items_async(
        self,
        plan_id: str,
        request: main_models.ListDisasterRecoveryItemsRequest,
    ) -> main_models.ListDisasterRecoveryItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_disaster_recovery_items_with_options_async(plan_id, request, headers, runtime)

    def list_disaster_recovery_plans_with_options(
        self,
        request: main_models.ListDisasterRecoveryPlansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDisasterRecoveryPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDisasterRecoveryPlans',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDisasterRecoveryPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_disaster_recovery_plans_with_options_async(
        self,
        request: main_models.ListDisasterRecoveryPlansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDisasterRecoveryPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDisasterRecoveryPlans',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDisasterRecoveryPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_disaster_recovery_plans(
        self,
        request: main_models.ListDisasterRecoveryPlansRequest,
    ) -> main_models.ListDisasterRecoveryPlansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_disaster_recovery_plans_with_options(request, headers, runtime)

    async def list_disaster_recovery_plans_async(
        self,
        request: main_models.ListDisasterRecoveryPlansRequest,
    ) -> main_models.ListDisasterRecoveryPlansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_disaster_recovery_plans_with_options_async(request, headers, runtime)

    def list_instance_account_with_options(
        self,
        instance_id: str,
        request: main_models.ListInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_status):
            query['accountStatus'] = request.account_status
        if not DaraCore.is_null(request.account_type):
            query['accountType'] = request.account_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.username):
            query['username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceAccount',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/accounts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_account_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_status):
            query['accountStatus'] = request.account_status
        if not DaraCore.is_null(request.account_type):
            query['accountType'] = request.account_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.username):
            query['username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceAccount',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/accounts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_account(
        self,
        instance_id: str,
        request: main_models.ListInstanceAccountRequest,
    ) -> main_models.ListInstanceAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_account_with_options(instance_id, request, headers, runtime)

    async def list_instance_account_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceAccountRequest,
    ) -> main_models.ListInstanceAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_account_with_options_async(instance_id, request, headers, runtime)

    def list_instance_acl_with_options(
        self,
        instance_id: str,
        request: main_models.ListInstanceAclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceAcl',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/acl',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_acl_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceAclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceAcl',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/acl',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_acl(
        self,
        instance_id: str,
        request: main_models.ListInstanceAclRequest,
    ) -> main_models.ListInstanceAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_acl_with_options(instance_id, request, headers, runtime)

    async def list_instance_acl_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceAclRequest,
    ) -> main_models.ListInstanceAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_acl_with_options_async(instance_id, request, headers, runtime)

    def list_instance_ip_whitelist_with_options(
        self,
        instance_id: str,
        request: main_models.ListInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceIpWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_whitelist):
            query['ipWhitelist'] = request.ip_whitelist
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceIpWhitelist',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/ip/whitelist',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_ip_whitelist_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceIpWhitelistRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceIpWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip_whitelist):
            query['ipWhitelist'] = request.ip_whitelist
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceIpWhitelist',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/ip/whitelist',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_ip_whitelist(
        self,
        instance_id: str,
        request: main_models.ListInstanceIpWhitelistRequest,
    ) -> main_models.ListInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instance_ip_whitelist_with_options(instance_id, request, headers, runtime)

    async def list_instance_ip_whitelist_async(
        self,
        instance_id: str,
        request: main_models.ListInstanceIpWhitelistRequest,
    ) -> main_models.ListInstanceIpWhitelistResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instance_ip_whitelist_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        tmp_req: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.series_codes):
            request.series_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.series_codes, 'seriesCodes', 'simple')
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.series_codes_shrink):
            query['seriesCodes'] = request.series_codes_shrink
        if not DaraCore.is_null(request.storage_secret_key):
            query['storageSecretKey'] = request.storage_secret_key
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        tmp_req: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.series_codes):
            request.series_codes_shrink = Utils.array_to_string_with_specified_style(tmp_req.series_codes, 'seriesCodes', 'simple')
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.series_codes_shrink):
            query['seriesCodes'] = request.series_codes_shrink
        if not DaraCore.is_null(request.storage_secret_key):
            query['storageSecretKey'] = request.storage_secret_key
        if not DaraCore.is_null(request.tags):
            query['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_messages_with_options(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.lite_topic_name):
            query['liteTopicName'] = request.lite_topic_name
        if not DaraCore.is_null(request.message_id):
            query['messageId'] = request.message_id
        if not DaraCore.is_null(request.message_key):
            query['messageKey'] = request.message_key
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.scroll_id):
            query['scrollId'] = request.scroll_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessages',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_messages_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.ListMessagesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMessagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.lite_topic_name):
            query['liteTopicName'] = request.lite_topic_name
        if not DaraCore.is_null(request.message_id):
            query['messageId'] = request.message_id
        if not DaraCore.is_null(request.message_key):
            query['messageKey'] = request.message_key
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.scroll_id):
            query['scrollId'] = request.scroll_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMessages',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/messages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_messages(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.ListMessagesRequest,
    ) -> main_models.ListMessagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_messages_with_options(instance_id, topic_name, request, headers, runtime)

    async def list_messages_async(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.ListMessagesRequest,
    ) -> main_models.ListMessagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_messages_with_options_async(instance_id, topic_name, request, headers, runtime)

    def list_metric_meta_with_options(
        self,
        request: main_models.ListMetricMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMetricMetaResponse:
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
            action = 'ListMetricMeta',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/monitor/metrics/meta',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMetricMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_metric_meta_with_options_async(
        self,
        request: main_models.ListMetricMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMetricMetaResponse:
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
            action = 'ListMetricMeta',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/monitor/metrics/meta',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMetricMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_metric_meta(
        self,
        request: main_models.ListMetricMetaRequest,
    ) -> main_models.ListMetricMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_metric_meta_with_options(request, headers, runtime)

    async def list_metric_meta_async(
        self,
        request: main_models.ListMetricMetaRequest,
    ) -> main_models.ListMetricMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_metric_meta_with_options_async(request, headers, runtime)

    def list_migration_operations_with_options(
        self,
        migration_id: str,
        stage_type: str,
        request: main_models.ListMigrationOperationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMigrationOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation_type):
            query['operationType'] = request.operation_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMigrationOperations',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/migrations/{DaraURL.percent_encode(migration_id)}/stages/{DaraURL.percent_encode(stage_type)}/operations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMigrationOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_migration_operations_with_options_async(
        self,
        migration_id: str,
        stage_type: str,
        request: main_models.ListMigrationOperationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMigrationOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.operation_type):
            query['operationType'] = request.operation_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMigrationOperations',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/migrations/{DaraURL.percent_encode(migration_id)}/stages/{DaraURL.percent_encode(stage_type)}/operations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMigrationOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_migration_operations(
        self,
        migration_id: str,
        stage_type: str,
        request: main_models.ListMigrationOperationsRequest,
    ) -> main_models.ListMigrationOperationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_migration_operations_with_options(migration_id, stage_type, request, headers, runtime)

    async def list_migration_operations_async(
        self,
        migration_id: str,
        stage_type: str,
        request: main_models.ListMigrationOperationsRequest,
    ) -> main_models.ListMigrationOperationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_migration_operations_with_options_async(migration_id, stage_type, request, headers, runtime)

    def list_migrations_with_options(
        self,
        request: main_models.ListMigrationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMigrationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.migration_type):
            query['migrationType'] = request.migration_type
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
            action = 'ListMigrations',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/migrations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMigrationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_migrations_with_options_async(
        self,
        request: main_models.ListMigrationsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMigrationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.migration_type):
            query['migrationType'] = request.migration_type
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
            action = 'ListMigrations',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/migrations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMigrationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_migrations(
        self,
        request: main_models.ListMigrationsRequest,
    ) -> main_models.ListMigrationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_migrations_with_options(request, headers, runtime)

    async def list_migrations_async(
        self,
        request: main_models.ListMigrationsRequest,
    ) -> main_models.ListMigrationsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_migrations_with_options_async(request, headers, runtime)

    def list_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_regions_with_options(headers, runtime)

    async def list_regions_async(self) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_regions_with_options_async(headers, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/resourceTag/list',
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
        request: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/resourceTag/list',
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

    def list_topic_subscriptions_with_options(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicSubscriptionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListTopicSubscriptions',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/subscriptions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topic_subscriptions_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicSubscriptionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListTopicSubscriptions',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/subscriptions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicSubscriptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topic_subscriptions(
        self,
        instance_id: str,
        topic_name: str,
    ) -> main_models.ListTopicSubscriptionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_topic_subscriptions_with_options(instance_id, topic_name, headers, runtime)

    async def list_topic_subscriptions_async(
        self,
        instance_id: str,
        topic_name: str,
    ) -> main_models.ListTopicSubscriptionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_topic_subscriptions_with_options_async(instance_id, topic_name, headers, runtime)

    def list_topics_with_options(
        self,
        instance_id: str,
        tmp_req: main_models.ListTopicsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicsResponse:
        tmp_req.validate()
        request = main_models.ListTopicsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.message_types):
            request.message_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.message_types, 'messageTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.message_types_shrink):
            query['messageTypes'] = request.message_types_shrink
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTopics',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topics_with_options_async(
        self,
        instance_id: str,
        tmp_req: main_models.ListTopicsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicsResponse:
        tmp_req.validate()
        request = main_models.ListTopicsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.message_types):
            request.message_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.message_types, 'messageTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.filter):
            query['filter'] = request.filter
        if not DaraCore.is_null(request.message_types_shrink):
            query['messageTypes'] = request.message_types_shrink
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTopics',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topics(
        self,
        instance_id: str,
        request: main_models.ListTopicsRequest,
    ) -> main_models.ListTopicsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_topics_with_options(instance_id, request, headers, runtime)

    async def list_topics_async(
        self,
        instance_id: str,
        request: main_models.ListTopicsRequest,
    ) -> main_models.ListTopicsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_topics_with_options_async(instance_id, request, headers, runtime)

    def list_traces_with_options(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.ListTracesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTracesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.lite_topic_name):
            query['liteTopicName'] = request.lite_topic_name
        if not DaraCore.is_null(request.message_id):
            query['messageId'] = request.message_id
        if not DaraCore.is_null(request.message_key):
            query['messageKey'] = request.message_key
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['queryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTraces',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/traces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traces_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.ListTracesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTracesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.lite_topic_name):
            query['liteTopicName'] = request.lite_topic_name
        if not DaraCore.is_null(request.message_id):
            query['messageId'] = request.message_id
        if not DaraCore.is_null(request.message_key):
            query['messageKey'] = request.message_key
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['queryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTraces',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/traces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traces(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.ListTracesRequest,
    ) -> main_models.ListTracesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_traces_with_options(instance_id, topic_name, request, headers, runtime)

    async def list_traces_async(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.ListTracesRequest,
    ) -> main_models.ListTracesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_traces_with_options_async(instance_id, topic_name, request, headers, runtime)

    def reset_consume_offset_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        request: main_models.ResetConsumeOffsetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetConsumeOffsetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.reset_time):
            body['resetTime'] = request.reset_time
        if not DaraCore.is_null(request.reset_type):
            body['resetType'] = request.reset_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetConsumeOffset',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/consumeOffsets/{DaraURL.percent_encode(topic_name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetConsumeOffsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_consume_offset_with_options_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        request: main_models.ResetConsumeOffsetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResetConsumeOffsetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.reset_time):
            body['resetTime'] = request.reset_time
        if not DaraCore.is_null(request.reset_type):
            body['resetType'] = request.reset_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetConsumeOffset',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}/consumeOffsets/{DaraURL.percent_encode(topic_name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetConsumeOffsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_consume_offset(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        request: main_models.ResetConsumeOffsetRequest,
    ) -> main_models.ResetConsumeOffsetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.reset_consume_offset_with_options(instance_id, consumer_group_id, topic_name, request, headers, runtime)

    async def reset_consume_offset_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        topic_name: str,
        request: main_models.ResetConsumeOffsetRequest,
    ) -> main_models.ResetConsumeOffsetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.reset_consume_offset_with_options_async(instance_id, consumer_group_id, topic_name, request, headers, runtime)

    def start_disaster_recovery_item_with_options(
        self,
        plan_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartDisasterRecoveryItemResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDisasterRecoveryItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_disaster_recovery_item_with_options_async(
        self,
        plan_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartDisasterRecoveryItemResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDisasterRecoveryItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_disaster_recovery_item(
        self,
        plan_id: str,
        item_id: str,
    ) -> main_models.StartDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_disaster_recovery_item_with_options(plan_id, item_id, headers, runtime)

    async def start_disaster_recovery_item_async(
        self,
        plan_id: str,
        item_id: str,
    ) -> main_models.StartDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_disaster_recovery_item_with_options_async(plan_id, item_id, headers, runtime)

    def stop_disaster_recovery_item_with_options(
        self,
        plan_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopDisasterRecoveryItemResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDisasterRecoveryItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_disaster_recovery_item_with_options_async(
        self,
        plan_id: str,
        item_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopDisasterRecoveryItemResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDisasterRecoveryItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_disaster_recovery_item(
        self,
        plan_id: str,
        item_id: str,
    ) -> main_models.StopDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_disaster_recovery_item_with_options(plan_id, item_id, headers, runtime)

    async def stop_disaster_recovery_item_async(
        self,
        plan_id: str,
        item_id: str,
    ) -> main_models.StopDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_disaster_recovery_item_with_options_async(plan_id, item_id, headers, runtime)

    def sync_disaster_recovery_checkpoint_with_options(
        self,
        plan_id: str,
        item_id: str,
        checkpoint_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncDisasterRecoveryCheckpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'SyncDisasterRecoveryCheckpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}/checkpoints/{DaraURL.percent_encode(checkpoint_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncDisasterRecoveryCheckpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_disaster_recovery_checkpoint_with_options_async(
        self,
        plan_id: str,
        item_id: str,
        checkpoint_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncDisasterRecoveryCheckpointResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'SyncDisasterRecoveryCheckpoint',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}/checkpoints/{DaraURL.percent_encode(checkpoint_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncDisasterRecoveryCheckpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_disaster_recovery_checkpoint(
        self,
        plan_id: str,
        item_id: str,
        checkpoint_id: str,
    ) -> main_models.SyncDisasterRecoveryCheckpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.sync_disaster_recovery_checkpoint_with_options(plan_id, item_id, checkpoint_id, headers, runtime)

    async def sync_disaster_recovery_checkpoint_async(
        self,
        plan_id: str,
        item_id: str,
        checkpoint_id: str,
    ) -> main_models.SyncDisasterRecoveryCheckpointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.sync_disaster_recovery_checkpoint_with_options_async(plan_id, item_id, checkpoint_id, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/resourceTag/create',
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
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/resourceTag/create',
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

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['tagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/resourceTag/delete',
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
        request: main_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['tagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/resourceTag/delete',
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

    def update_consumer_group_with_options(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.consume_retry_policy):
            body['consumeRetryPolicy'] = request.consume_retry_policy
        if not DaraCore.is_null(request.delivery_order_type):
            body['deliveryOrderType'] = request.delivery_order_type
        if not DaraCore.is_null(request.max_receive_tps):
            body['maxReceiveTps'] = request.max_receive_tps
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerGroup',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}',
            method = 'PATCH',
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
        instance_id: str,
        consumer_group_id: str,
        request: main_models.UpdateConsumerGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConsumerGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.consume_retry_policy):
            body['consumeRetryPolicy'] = request.consume_retry_policy
        if not DaraCore.is_null(request.delivery_order_type):
            body['deliveryOrderType'] = request.delivery_order_type
        if not DaraCore.is_null(request.max_receive_tps):
            body['maxReceiveTps'] = request.max_receive_tps
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConsumerGroup',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/consumerGroups/{DaraURL.percent_encode(consumer_group_id)}',
            method = 'PATCH',
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
        instance_id: str,
        consumer_group_id: str,
        request: main_models.UpdateConsumerGroupRequest,
    ) -> main_models.UpdateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_consumer_group_with_options(instance_id, consumer_group_id, request, headers, runtime)

    async def update_consumer_group_async(
        self,
        instance_id: str,
        consumer_group_id: str,
        request: main_models.UpdateConsumerGroupRequest,
    ) -> main_models.UpdateConsumerGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_consumer_group_with_options_async(instance_id, consumer_group_id, request, headers, runtime)

    def update_disaster_recovery_item_with_options(
        self,
        plan_id: str,
        item_id: str,
        request: main_models.UpdateDisasterRecoveryItemRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDisasterRecoveryItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.topics):
            body['topics'] = request.topics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDisasterRecoveryItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_disaster_recovery_item_with_options_async(
        self,
        plan_id: str,
        item_id: str,
        request: main_models.UpdateDisasterRecoveryItemRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDisasterRecoveryItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.topics):
            body['topics'] = request.topics
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDisasterRecoveryItem',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}/items/{DaraURL.percent_encode(item_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDisasterRecoveryItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_disaster_recovery_item(
        self,
        plan_id: str,
        item_id: str,
        request: main_models.UpdateDisasterRecoveryItemRequest,
    ) -> main_models.UpdateDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_disaster_recovery_item_with_options(plan_id, item_id, request, headers, runtime)

    async def update_disaster_recovery_item_async(
        self,
        plan_id: str,
        item_id: str,
        request: main_models.UpdateDisasterRecoveryItemRequest,
    ) -> main_models.UpdateDisasterRecoveryItemResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_disaster_recovery_item_with_options_async(plan_id, item_id, request, headers, runtime)

    def update_disaster_recovery_plan_with_options(
        self,
        plan_id: str,
        request: main_models.UpdateDisasterRecoveryPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDisasterRecoveryPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_sync_checkpoint):
            body['autoSyncCheckpoint'] = request.auto_sync_checkpoint
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.plan_desc):
            body['planDesc'] = request.plan_desc
        if not DaraCore.is_null(request.plan_name):
            body['planName'] = request.plan_name
        if not DaraCore.is_null(request.plan_type):
            body['planType'] = request.plan_type
        if not DaraCore.is_null(request.sync_checkpoint_enabled):
            body['syncCheckpointEnabled'] = request.sync_checkpoint_enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDisasterRecoveryPlan',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDisasterRecoveryPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_disaster_recovery_plan_with_options_async(
        self,
        plan_id: str,
        request: main_models.UpdateDisasterRecoveryPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDisasterRecoveryPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_sync_checkpoint):
            body['autoSyncCheckpoint'] = request.auto_sync_checkpoint
        if not DaraCore.is_null(request.instances):
            body['instances'] = request.instances
        if not DaraCore.is_null(request.plan_desc):
            body['planDesc'] = request.plan_desc
        if not DaraCore.is_null(request.plan_name):
            body['planName'] = request.plan_name
        if not DaraCore.is_null(request.plan_type):
            body['planType'] = request.plan_type
        if not DaraCore.is_null(request.sync_checkpoint_enabled):
            body['syncCheckpointEnabled'] = request.sync_checkpoint_enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDisasterRecoveryPlan',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/disaster_recovery/{DaraURL.percent_encode(plan_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDisasterRecoveryPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_disaster_recovery_plan(
        self,
        plan_id: str,
        request: main_models.UpdateDisasterRecoveryPlanRequest,
    ) -> main_models.UpdateDisasterRecoveryPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_disaster_recovery_plan_with_options(plan_id, request, headers, runtime)

    async def update_disaster_recovery_plan_async(
        self,
        plan_id: str,
        request: main_models.UpdateDisasterRecoveryPlanRequest,
    ) -> main_models.UpdateDisasterRecoveryPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_disaster_recovery_plan_with_options_async(plan_id, request, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acl_info):
            body['aclInfo'] = request.acl_info
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.network_info):
            body['networkInfo'] = request.network_info
        if not DaraCore.is_null(request.product_info):
            body['productInfo'] = request.product_info
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acl_info):
            body['aclInfo'] = request.acl_info
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.network_info):
            body['networkInfo'] = request.network_info
        if not DaraCore.is_null(request.product_info):
            body['productInfo'] = request.product_info
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)

    def update_instance_account_with_options(
        self,
        instance_id: str,
        username: str,
        request: main_models.UpdateInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_status):
            query['accountStatus'] = request.account_status
        if not DaraCore.is_null(request.password):
            query['password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceAccount',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/accounts/{DaraURL.percent_encode(username)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_account_with_options_async(
        self,
        instance_id: str,
        username: str,
        request: main_models.UpdateInstanceAccountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_status):
            query['accountStatus'] = request.account_status
        if not DaraCore.is_null(request.password):
            query['password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceAccount',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/accounts/{DaraURL.percent_encode(username)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_account(
        self,
        instance_id: str,
        username: str,
        request: main_models.UpdateInstanceAccountRequest,
    ) -> main_models.UpdateInstanceAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_account_with_options(instance_id, username, request, headers, runtime)

    async def update_instance_account_async(
        self,
        instance_id: str,
        username: str,
        request: main_models.UpdateInstanceAccountRequest,
    ) -> main_models.UpdateInstanceAccountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_account_with_options_async(instance_id, username, request, headers, runtime)

    def update_instance_acl_with_options(
        self,
        instance_id: str,
        username: str,
        request: main_models.UpdateInstanceAclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceAclResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.actions):
            body['actions'] = request.actions
        if not DaraCore.is_null(request.decision):
            body['decision'] = request.decision
        if not DaraCore.is_null(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        if not DaraCore.is_null(request.resource_name):
            body['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceAcl',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/acl/account/{DaraURL.percent_encode(username)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_acl_with_options_async(
        self,
        instance_id: str,
        username: str,
        request: main_models.UpdateInstanceAclRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceAclResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.actions):
            body['actions'] = request.actions
        if not DaraCore.is_null(request.decision):
            body['decision'] = request.decision
        if not DaraCore.is_null(request.ip_whitelists):
            body['ipWhitelists'] = request.ip_whitelists
        if not DaraCore.is_null(request.resource_name):
            body['resourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceAcl',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/acl/account/{DaraURL.percent_encode(username)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_acl(
        self,
        instance_id: str,
        username: str,
        request: main_models.UpdateInstanceAclRequest,
    ) -> main_models.UpdateInstanceAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_acl_with_options(instance_id, username, request, headers, runtime)

    async def update_instance_acl_async(
        self,
        instance_id: str,
        username: str,
        request: main_models.UpdateInstanceAclRequest,
    ) -> main_models.UpdateInstanceAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_acl_with_options_async(instance_id, username, request, headers, runtime)

    def update_topic_with_options(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.UpdateTopicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTopicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lite_topic_expiration):
            body['liteTopicExpiration'] = request.lite_topic_expiration
        if not DaraCore.is_null(request.max_send_tps):
            body['maxSendTps'] = request.max_send_tps
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTopic',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_topic_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.UpdateTopicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTopicResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lite_topic_expiration):
            body['liteTopicExpiration'] = request.lite_topic_expiration
        if not DaraCore.is_null(request.max_send_tps):
            body['maxSendTps'] = request.max_send_tps
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTopic',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}',
            method = 'PATCH',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_topic(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.UpdateTopicRequest,
    ) -> main_models.UpdateTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_topic_with_options(instance_id, topic_name, request, headers, runtime)

    async def update_topic_async(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.UpdateTopicRequest,
    ) -> main_models.UpdateTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_topic_with_options_async(instance_id, topic_name, request, headers, runtime)

    def verify_consume_message_with_options(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: main_models.VerifyConsumeMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.VerifyConsumeMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.consumer_group_id):
            query['consumerGroupId'] = request.consumer_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyConsumeMessage',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/messages/{DaraURL.percent_encode(message_id)}/action/verifyConsume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyConsumeMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_consume_message_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: main_models.VerifyConsumeMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.VerifyConsumeMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.consumer_group_id):
            query['consumerGroupId'] = request.consumer_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyConsumeMessage',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/messages/{DaraURL.percent_encode(message_id)}/action/verifyConsume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyConsumeMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_consume_message(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: main_models.VerifyConsumeMessageRequest,
    ) -> main_models.VerifyConsumeMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.verify_consume_message_with_options(instance_id, topic_name, message_id, request, headers, runtime)

    async def verify_consume_message_async(
        self,
        instance_id: str,
        topic_name: str,
        message_id: str,
        request: main_models.VerifyConsumeMessageRequest,
    ) -> main_models.VerifyConsumeMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.verify_consume_message_with_options_async(instance_id, topic_name, message_id, request, headers, runtime)

    def verify_send_message_with_options(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.VerifySendMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.VerifySendMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lite_topic_name):
            body['liteTopicName'] = request.lite_topic_name
        if not DaraCore.is_null(request.message):
            body['message'] = request.message
        if not DaraCore.is_null(request.message_key):
            body['messageKey'] = request.message_key
        if not DaraCore.is_null(request.message_tag):
            body['messageTag'] = request.message_tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VerifySendMessage',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/messages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifySendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_send_message_with_options_async(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.VerifySendMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.VerifySendMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lite_topic_name):
            body['liteTopicName'] = request.lite_topic_name
        if not DaraCore.is_null(request.message):
            body['message'] = request.message
        if not DaraCore.is_null(request.message_key):
            body['messageKey'] = request.message_key
        if not DaraCore.is_null(request.message_tag):
            body['messageTag'] = request.message_tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'VerifySendMessage',
            version = '2022-08-01',
            protocol = 'HTTPS',
            pathname = f'/instances/{DaraURL.percent_encode(instance_id)}/topics/{DaraURL.percent_encode(topic_name)}/messages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifySendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_send_message(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.VerifySendMessageRequest,
    ) -> main_models.VerifySendMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.verify_send_message_with_options(instance_id, topic_name, request, headers, runtime)

    async def verify_send_message_async(
        self,
        instance_id: str,
        topic_name: str,
        request: main_models.VerifySendMessageRequest,
    ) -> main_models.VerifySendMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.verify_send_message_with_options_async(instance_id, topic_name, request, headers, runtime)
