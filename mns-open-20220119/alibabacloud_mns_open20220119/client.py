# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_mns_open20220119 import models as main_models
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
            'us-west-1': 'mns-open.us-west-1.aliyuncs.com',
            'us-east-1': 'mns-open.us-east-1.aliyuncs.com',
            'me-east-1': 'mns-open.me-east-1.aliyuncs.com',
            'me-central-1': 'mns-open.me-central-1.aliyuncs.com',
            'eu-west-1': 'mns-open.eu-west-1.aliyuncs.com',
            'eu-central-1': 'mns-open.eu-central-1.aliyuncs.com',
            'cn-zhengzhou-jva': 'mns-open.cn-zhengzhou-jva.aliyuncs.com',
            'cn-zhangjiakou': 'mns-open.cn-zhangjiakou.aliyuncs.com',
            'cn-wulanchabu': 'mns-open.cn-wulanchabu.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mns-open.cn-shenzhen-finance-1.aliyuncs.com',
            'cn-shenzhen': 'mns-open.cn-shenzhen.aliyuncs.com',
            'cn-shanghai-finance-1': 'mns-open.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shanghai': 'mns-open.cn-shanghai.aliyuncs.com',
            'cn-qingdao': 'mns-open.cn-qingdao.aliyuncs.com',
            'cn-huhehaote': 'mns-open.cn-huhehaote.aliyuncs.com',
            'cn-hongkong': 'mns-open.cn-hongkong.aliyuncs.com',
            'cn-heyuan-acdr-1': 'mns-open.cn-heyuan-acdr-1.aliyuncs.com',
            'cn-heyuan': 'mns-open.cn-heyuan.aliyuncs.com',
            'cn-hangzhou-finance': 'mns-open.cn-hangzhou-finance.aliyuncs.com',
            'cn-hangzhou': 'mns-open.cn-hangzhou.aliyuncs.com',
            'cn-guangzhou': 'mns-open.cn-guangzhou.aliyuncs.com',
            'cn-chengdu': 'mns-open.cn-chengdu.aliyuncs.com',
            'cn-beijing': 'mns-open.cn-beijing.aliyuncs.com',
            'ap-southeast-7': 'mns-open.ap-southeast-7.aliyuncs.com',
            'ap-southeast-5': 'mns-open.ap-southeast-5.aliyuncs.com',
            'ap-southeast-3': 'mns-open.ap-southeast-3.aliyuncs.com',
            'ap-southeast-1': 'mns-open.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2': 'mns-open.ap-northeast-2.aliyuncs.com',
            'ap-northeast-1': 'mns-open.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('mns-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def authorize_endpoint_acl_with_options(
        self,
        tmp_req: main_models.AuthorizeEndpointAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeEndpointAclResponse:
        tmp_req.validate()
        request = main_models.AuthorizeEndpointAclShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cidr_list):
            request.cidr_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.cidr_list, 'CidrList', 'simple')
        query = {}
        if not DaraCore.is_null(request.acl_strategy):
            query['AclStrategy'] = request.acl_strategy
        if not DaraCore.is_null(request.cidr_list_shrink):
            query['CidrList'] = request.cidr_list_shrink
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeEndpointAcl',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeEndpointAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_endpoint_acl_with_options_async(
        self,
        tmp_req: main_models.AuthorizeEndpointAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeEndpointAclResponse:
        tmp_req.validate()
        request = main_models.AuthorizeEndpointAclShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cidr_list):
            request.cidr_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.cidr_list, 'CidrList', 'simple')
        query = {}
        if not DaraCore.is_null(request.acl_strategy):
            query['AclStrategy'] = request.acl_strategy
        if not DaraCore.is_null(request.cidr_list_shrink):
            query['CidrList'] = request.cidr_list_shrink
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeEndpointAcl',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeEndpointAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_endpoint_acl(
        self,
        request: main_models.AuthorizeEndpointAclRequest,
    ) -> main_models.AuthorizeEndpointAclResponse:
        runtime = RuntimeOptions()
        return self.authorize_endpoint_acl_with_options(request, runtime)

    async def authorize_endpoint_acl_async(
        self,
        request: main_models.AuthorizeEndpointAclRequest,
    ) -> main_models.AuthorizeEndpointAclResponse:
        runtime = RuntimeOptions()
        return await self.authorize_endpoint_acl_with_options_async(request, runtime)

    def create_event_rule_with_options(
        self,
        tmp_req: main_models.CreateEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventRuleResponse:
        tmp_req.validate()
        request = main_models.CreateEventRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.endpoint):
            request.endpoint_shrink = Utils.array_to_string_with_specified_style(tmp_req.endpoint, 'Endpoint', 'json')
        if not DaraCore.is_null(tmp_req.endpoints):
            request.endpoints_shrink = Utils.array_to_string_with_specified_style(tmp_req.endpoints, 'Endpoints', 'json')
        if not DaraCore.is_null(tmp_req.event_types):
            request.event_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_types, 'EventTypes', 'json')
        if not DaraCore.is_null(tmp_req.match_rules):
            request.match_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_rules, 'MatchRules', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delivery_mode):
            query['DeliveryMode'] = request.delivery_mode
        if not DaraCore.is_null(request.endpoint_shrink):
            query['Endpoint'] = request.endpoint_shrink
        if not DaraCore.is_null(request.endpoints_shrink):
            query['Endpoints'] = request.endpoints_shrink
        if not DaraCore.is_null(request.event_types_shrink):
            query['EventTypes'] = request.event_types_shrink
        if not DaraCore.is_null(request.match_rules_shrink):
            query['MatchRules'] = request.match_rules_shrink
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventRule',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_rule_with_options_async(
        self,
        tmp_req: main_models.CreateEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEventRuleResponse:
        tmp_req.validate()
        request = main_models.CreateEventRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.endpoint):
            request.endpoint_shrink = Utils.array_to_string_with_specified_style(tmp_req.endpoint, 'Endpoint', 'json')
        if not DaraCore.is_null(tmp_req.endpoints):
            request.endpoints_shrink = Utils.array_to_string_with_specified_style(tmp_req.endpoints, 'Endpoints', 'json')
        if not DaraCore.is_null(tmp_req.event_types):
            request.event_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.event_types, 'EventTypes', 'json')
        if not DaraCore.is_null(tmp_req.match_rules):
            request.match_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_rules, 'MatchRules', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.delivery_mode):
            query['DeliveryMode'] = request.delivery_mode
        if not DaraCore.is_null(request.endpoint_shrink):
            query['Endpoint'] = request.endpoint_shrink
        if not DaraCore.is_null(request.endpoints_shrink):
            query['Endpoints'] = request.endpoints_shrink
        if not DaraCore.is_null(request.event_types_shrink):
            query['EventTypes'] = request.event_types_shrink
        if not DaraCore.is_null(request.match_rules_shrink):
            query['MatchRules'] = request.match_rules_shrink
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateEventRule',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEventRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event_rule(
        self,
        request: main_models.CreateEventRuleRequest,
    ) -> main_models.CreateEventRuleResponse:
        runtime = RuntimeOptions()
        return self.create_event_rule_with_options(request, runtime)

    async def create_event_rule_async(
        self,
        request: main_models.CreateEventRuleRequest,
    ) -> main_models.CreateEventRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_event_rule_with_options_async(request, runtime)

    def create_queue_with_options(
        self,
        tmp_req: main_models.CreateQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueueResponse:
        tmp_req.validate()
        request = main_models.CreateQueueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dlq_policy):
            request.dlq_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        if not DaraCore.is_null(tmp_req.tenant_rate_limit_policy):
            request.tenant_rate_limit_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_rate_limit_policy, 'TenantRateLimitPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.delay_seconds):
            query['DelaySeconds'] = request.delay_seconds
        if not DaraCore.is_null(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not DaraCore.is_null(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not DaraCore.is_null(request.enable_sse):
            query['EnableSSE'] = request.enable_sse
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.maximum_message_size):
            query['MaximumMessageSize'] = request.maximum_message_size
        if not DaraCore.is_null(request.message_retention_period):
            query['MessageRetentionPeriod'] = request.message_retention_period
        if not DaraCore.is_null(request.polling_wait_seconds):
            query['PollingWaitSeconds'] = request.polling_wait_seconds
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.queue_type):
            query['QueueType'] = request.queue_type
        if not DaraCore.is_null(request.sse_algorithm):
            query['SseAlgorithm'] = request.sse_algorithm
        if not DaraCore.is_null(request.sse_type):
            query['SseType'] = request.sse_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tenant_rate_limit_policy_shrink):
            query['TenantRateLimitPolicy'] = request.tenant_rate_limit_policy_shrink
        if not DaraCore.is_null(request.visibility_timeout):
            query['VisibilityTimeout'] = request.visibility_timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueue',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_queue_with_options_async(
        self,
        tmp_req: main_models.CreateQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQueueResponse:
        tmp_req.validate()
        request = main_models.CreateQueueShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dlq_policy):
            request.dlq_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        if not DaraCore.is_null(tmp_req.tenant_rate_limit_policy):
            request.tenant_rate_limit_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_rate_limit_policy, 'TenantRateLimitPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.delay_seconds):
            query['DelaySeconds'] = request.delay_seconds
        if not DaraCore.is_null(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not DaraCore.is_null(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not DaraCore.is_null(request.enable_sse):
            query['EnableSSE'] = request.enable_sse
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.maximum_message_size):
            query['MaximumMessageSize'] = request.maximum_message_size
        if not DaraCore.is_null(request.message_retention_period):
            query['MessageRetentionPeriod'] = request.message_retention_period
        if not DaraCore.is_null(request.polling_wait_seconds):
            query['PollingWaitSeconds'] = request.polling_wait_seconds
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.queue_type):
            query['QueueType'] = request.queue_type
        if not DaraCore.is_null(request.sse_algorithm):
            query['SseAlgorithm'] = request.sse_algorithm
        if not DaraCore.is_null(request.sse_type):
            query['SseType'] = request.sse_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tenant_rate_limit_policy_shrink):
            query['TenantRateLimitPolicy'] = request.tenant_rate_limit_policy_shrink
        if not DaraCore.is_null(request.visibility_timeout):
            query['VisibilityTimeout'] = request.visibility_timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQueue',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_queue(
        self,
        request: main_models.CreateQueueRequest,
    ) -> main_models.CreateQueueResponse:
        runtime = RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    async def create_queue_async(
        self,
        request: main_models.CreateQueueRequest,
    ) -> main_models.CreateQueueResponse:
        runtime = RuntimeOptions()
        return await self.create_queue_with_options_async(request, runtime)

    def create_topic_with_options(
        self,
        request: main_models.CreateTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic_type):
            query['TopicType'] = request.topic_type
        body = {}
        if not DaraCore.is_null(request.enable_logging):
            body['EnableLogging'] = request.enable_logging
        if not DaraCore.is_null(request.enable_sse):
            body['EnableSSE'] = request.enable_sse
        if not DaraCore.is_null(request.kms_key_id):
            body['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.max_message_size):
            body['MaxMessageSize'] = request.max_message_size
        if not DaraCore.is_null(request.sse_algorithm):
            body['SseAlgorithm'] = request.sse_algorithm
        if not DaraCore.is_null(request.sse_type):
            body['SseType'] = request.sse_type
        if not DaraCore.is_null(request.topic_name):
            body['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTopic',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_topic_with_options_async(
        self,
        request: main_models.CreateTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic_type):
            query['TopicType'] = request.topic_type
        body = {}
        if not DaraCore.is_null(request.enable_logging):
            body['EnableLogging'] = request.enable_logging
        if not DaraCore.is_null(request.enable_sse):
            body['EnableSSE'] = request.enable_sse
        if not DaraCore.is_null(request.kms_key_id):
            body['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.max_message_size):
            body['MaxMessageSize'] = request.max_message_size
        if not DaraCore.is_null(request.sse_algorithm):
            body['SseAlgorithm'] = request.sse_algorithm
        if not DaraCore.is_null(request.sse_type):
            body['SseType'] = request.sse_type
        if not DaraCore.is_null(request.topic_name):
            body['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTopic',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_topic(
        self,
        request: main_models.CreateTopicRequest,
    ) -> main_models.CreateTopicResponse:
        runtime = RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    async def create_topic_async(
        self,
        request: main_models.CreateTopicRequest,
    ) -> main_models.CreateTopicResponse:
        runtime = RuntimeOptions()
        return await self.create_topic_with_options_async(request, runtime)

    def delete_event_rule_with_options(
        self,
        request: main_models.DeleteEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventRule',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_rule_with_options_async(
        self,
        request: main_models.DeleteEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventRule',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_rule(
        self,
        request: main_models.DeleteEventRuleRequest,
    ) -> main_models.DeleteEventRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_event_rule_with_options(request, runtime)

    async def delete_event_rule_async(
        self,
        request: main_models.DeleteEventRuleRequest,
    ) -> main_models.DeleteEventRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_rule_with_options_async(request, runtime)

    def delete_queue_with_options(
        self,
        request: main_models.DeleteQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQueue',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_queue_with_options_async(
        self,
        request: main_models.DeleteQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQueue',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_queue(
        self,
        request: main_models.DeleteQueueRequest,
    ) -> main_models.DeleteQueueResponse:
        runtime = RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    async def delete_queue_async(
        self,
        request: main_models.DeleteQueueRequest,
    ) -> main_models.DeleteQueueResponse:
        runtime = RuntimeOptions()
        return await self.delete_queue_with_options_async(request, runtime)

    def delete_topic_with_options(
        self,
        request: main_models.DeleteTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTopic',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_topic_with_options_async(
        self,
        request: main_models.DeleteTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTopic',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_topic(
        self,
        request: main_models.DeleteTopicRequest,
    ) -> main_models.DeleteTopicResponse:
        runtime = RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    async def delete_topic_async(
        self,
        request: main_models.DeleteTopicRequest,
    ) -> main_models.DeleteTopicResponse:
        runtime = RuntimeOptions()
        return await self.delete_topic_with_options_async(request, runtime)

    def disable_endpoint_with_options(
        self,
        request: main_models.DisableEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableEndpoint',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_endpoint_with_options_async(
        self,
        request: main_models.DisableEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableEndpoint',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_endpoint(
        self,
        request: main_models.DisableEndpointRequest,
    ) -> main_models.DisableEndpointResponse:
        runtime = RuntimeOptions()
        return self.disable_endpoint_with_options(request, runtime)

    async def disable_endpoint_async(
        self,
        request: main_models.DisableEndpointRequest,
    ) -> main_models.DisableEndpointResponse:
        runtime = RuntimeOptions()
        return await self.disable_endpoint_with_options_async(request, runtime)

    def enable_endpoint_with_options(
        self,
        request: main_models.EnableEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableEndpoint',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_endpoint_with_options_async(
        self,
        request: main_models.EnableEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableEndpoint',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_endpoint(
        self,
        request: main_models.EnableEndpointRequest,
    ) -> main_models.EnableEndpointResponse:
        runtime = RuntimeOptions()
        return self.enable_endpoint_with_options(request, runtime)

    async def enable_endpoint_async(
        self,
        request: main_models.EnableEndpointRequest,
    ) -> main_models.EnableEndpointResponse:
        runtime = RuntimeOptions()
        return await self.enable_endpoint_with_options_async(request, runtime)

    def get_endpoint_attribute_with_options(
        self,
        request: main_models.GetEndpointAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEndpointAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEndpointAttribute',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEndpointAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_endpoint_attribute_with_options_async(
        self,
        request: main_models.GetEndpointAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEndpointAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEndpointAttribute',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEndpointAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_endpoint_attribute(
        self,
        request: main_models.GetEndpointAttributeRequest,
    ) -> main_models.GetEndpointAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_endpoint_attribute_with_options(request, runtime)

    async def get_endpoint_attribute_async(
        self,
        request: main_models.GetEndpointAttributeRequest,
    ) -> main_models.GetEndpointAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_endpoint_attribute_with_options_async(request, runtime)

    def get_event_rule_with_options(
        self,
        request: main_models.GetEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEventRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEventRule',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_rule_with_options_async(
        self,
        request: main_models.GetEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEventRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEventRule',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEventRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_rule(
        self,
        request: main_models.GetEventRuleRequest,
    ) -> main_models.GetEventRuleResponse:
        runtime = RuntimeOptions()
        return self.get_event_rule_with_options(request, runtime)

    async def get_event_rule_async(
        self,
        request: main_models.GetEventRuleRequest,
    ) -> main_models.GetEventRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_event_rule_with_options_async(request, runtime)

    def get_queue_attributes_with_options(
        self,
        request: main_models.GetQueueAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_attributes_with_options_async(
        self,
        request: main_models.GetQueueAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQueueAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQueueAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQueueAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_queue_attributes(
        self,
        request: main_models.GetQueueAttributesRequest,
    ) -> main_models.GetQueueAttributesResponse:
        runtime = RuntimeOptions()
        return self.get_queue_attributes_with_options(request, runtime)

    async def get_queue_attributes_async(
        self,
        request: main_models.GetQueueAttributesRequest,
    ) -> main_models.GetQueueAttributesResponse:
        runtime = RuntimeOptions()
        return await self.get_queue_attributes_with_options_async(request, runtime)

    def get_subscription_attributes_with_options(
        self,
        request: main_models.GetSubscriptionAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubscriptionAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_attributes_with_options_async(
        self,
        request: main_models.GetSubscriptionAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubscriptionAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription_attributes(
        self,
        request: main_models.GetSubscriptionAttributesRequest,
    ) -> main_models.GetSubscriptionAttributesResponse:
        runtime = RuntimeOptions()
        return self.get_subscription_attributes_with_options(request, runtime)

    async def get_subscription_attributes_async(
        self,
        request: main_models.GetSubscriptionAttributesRequest,
    ) -> main_models.GetSubscriptionAttributesResponse:
        runtime = RuntimeOptions()
        return await self.get_subscription_attributes_with_options_async(request, runtime)

    def get_topic_attributes_with_options(
        self,
        request: main_models.GetTopicAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_attributes_with_options_async(
        self,
        request: main_models.GetTopicAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTopicAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTopicAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTopicAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic_attributes(
        self,
        request: main_models.GetTopicAttributesRequest,
    ) -> main_models.GetTopicAttributesResponse:
        runtime = RuntimeOptions()
        return self.get_topic_attributes_with_options(request, runtime)

    async def get_topic_attributes_async(
        self,
        request: main_models.GetTopicAttributesRequest,
    ) -> main_models.GetTopicAttributesResponse:
        runtime = RuntimeOptions()
        return await self.get_topic_attributes_with_options_async(request, runtime)

    def list_event_rules_with_options(
        self,
        tmp_req: main_models.ListEventRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventRulesResponse:
        tmp_req.validate()
        request = main_models.ListEventRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.subscription):
            request.subscription_shrink = Utils.array_to_string_with_specified_style(tmp_req.subscription, 'Subscription', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.subscription_shrink):
            query['Subscription'] = request.subscription_shrink
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEventRules',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_rules_with_options_async(
        self,
        tmp_req: main_models.ListEventRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventRulesResponse:
        tmp_req.validate()
        request = main_models.ListEventRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.subscription):
            request.subscription_shrink = Utils.array_to_string_with_specified_style(tmp_req.subscription, 'Subscription', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.subscription_shrink):
            query['Subscription'] = request.subscription_shrink
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEventRules',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_rules(
        self,
        request: main_models.ListEventRulesRequest,
    ) -> main_models.ListEventRulesResponse:
        runtime = RuntimeOptions()
        return self.list_event_rules_with_options(request, runtime)

    async def list_event_rules_async(
        self,
        request: main_models.ListEventRulesRequest,
    ) -> main_models.ListEventRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_event_rules_with_options_async(request, runtime)

    def list_queue_with_options(
        self,
        request: main_models.ListQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.queue_type):
            query['QueueType'] = request.queue_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueue',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_queue_with_options_async(
        self,
        request: main_models.ListQueueRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQueueResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.queue_type):
            query['QueueType'] = request.queue_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQueue',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQueueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_queue(
        self,
        request: main_models.ListQueueRequest,
    ) -> main_models.ListQueueResponse:
        runtime = RuntimeOptions()
        return self.list_queue_with_options(request, runtime)

    async def list_queue_async(
        self,
        request: main_models.ListQueueRequest,
    ) -> main_models.ListQueueResponse:
        runtime = RuntimeOptions()
        return await self.list_queue_with_options_async(request, runtime)

    def list_subscription_by_topic_with_options(
        self,
        request: main_models.ListSubscriptionByTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubscriptionByTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.endpoint_value):
            query['EndpointValue'] = request.endpoint_value
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubscriptionByTopic',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubscriptionByTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subscription_by_topic_with_options_async(
        self,
        request: main_models.ListSubscriptionByTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSubscriptionByTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.endpoint_value):
            query['EndpointValue'] = request.endpoint_value
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSubscriptionByTopic',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubscriptionByTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subscription_by_topic(
        self,
        request: main_models.ListSubscriptionByTopicRequest,
    ) -> main_models.ListSubscriptionByTopicResponse:
        runtime = RuntimeOptions()
        return self.list_subscription_by_topic_with_options(request, runtime)

    async def list_subscription_by_topic_async(
        self,
        request: main_models.ListSubscriptionByTopicRequest,
    ) -> main_models.ListSubscriptionByTopicResponse:
        runtime = RuntimeOptions()
        return await self.list_subscription_by_topic_with_options_async(request, runtime)

    def list_topic_with_options(
        self,
        request: main_models.ListTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        if not DaraCore.is_null(request.topic_type):
            query['TopicType'] = request.topic_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTopic',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topic_with_options_async(
        self,
        request: main_models.ListTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        if not DaraCore.is_null(request.topic_type):
            query['TopicType'] = request.topic_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTopic',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topic(
        self,
        request: main_models.ListTopicRequest,
    ) -> main_models.ListTopicResponse:
        runtime = RuntimeOptions()
        return self.list_topic_with_options(request, runtime)

    async def list_topic_async(
        self,
        request: main_models.ListTopicRequest,
    ) -> main_models.ListTopicResponse:
        runtime = RuntimeOptions()
        return await self.list_topic_with_options_async(request, runtime)

    def revoke_endpoint_acl_with_options(
        self,
        tmp_req: main_models.RevokeEndpointAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeEndpointAclResponse:
        tmp_req.validate()
        request = main_models.RevokeEndpointAclShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cidr_list):
            request.cidr_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.cidr_list, 'CidrList', 'simple')
        query = {}
        if not DaraCore.is_null(request.acl_strategy):
            query['AclStrategy'] = request.acl_strategy
        if not DaraCore.is_null(request.cidr_list_shrink):
            query['CidrList'] = request.cidr_list_shrink
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeEndpointAcl',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeEndpointAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_endpoint_acl_with_options_async(
        self,
        tmp_req: main_models.RevokeEndpointAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeEndpointAclResponse:
        tmp_req.validate()
        request = main_models.RevokeEndpointAclShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cidr_list):
            request.cidr_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.cidr_list, 'CidrList', 'simple')
        query = {}
        if not DaraCore.is_null(request.acl_strategy):
            query['AclStrategy'] = request.acl_strategy
        if not DaraCore.is_null(request.cidr_list_shrink):
            query['CidrList'] = request.cidr_list_shrink
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeEndpointAcl',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeEndpointAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_endpoint_acl(
        self,
        request: main_models.RevokeEndpointAclRequest,
    ) -> main_models.RevokeEndpointAclResponse:
        runtime = RuntimeOptions()
        return self.revoke_endpoint_acl_with_options(request, runtime)

    async def revoke_endpoint_acl_async(
        self,
        request: main_models.RevokeEndpointAclRequest,
    ) -> main_models.RevokeEndpointAclResponse:
        runtime = RuntimeOptions()
        return await self.revoke_endpoint_acl_with_options_async(request, runtime)

    def set_queue_attributes_with_options(
        self,
        tmp_req: main_models.SetQueueAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetQueueAttributesResponse:
        tmp_req.validate()
        request = main_models.SetQueueAttributesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dlq_policy):
            request.dlq_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        if not DaraCore.is_null(tmp_req.tenant_rate_limit_policy):
            request.tenant_rate_limit_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_rate_limit_policy, 'TenantRateLimitPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.delay_seconds):
            query['DelaySeconds'] = request.delay_seconds
        if not DaraCore.is_null(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not DaraCore.is_null(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not DaraCore.is_null(request.enable_sse):
            query['EnableSSE'] = request.enable_sse
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.maximum_message_size):
            query['MaximumMessageSize'] = request.maximum_message_size
        if not DaraCore.is_null(request.message_retention_period):
            query['MessageRetentionPeriod'] = request.message_retention_period
        if not DaraCore.is_null(request.polling_wait_seconds):
            query['PollingWaitSeconds'] = request.polling_wait_seconds
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.sse_algorithm):
            query['SseAlgorithm'] = request.sse_algorithm
        if not DaraCore.is_null(request.sse_type):
            query['SseType'] = request.sse_type
        if not DaraCore.is_null(request.tenant_rate_limit_policy_shrink):
            query['TenantRateLimitPolicy'] = request.tenant_rate_limit_policy_shrink
        if not DaraCore.is_null(request.visibility_timeout):
            query['VisibilityTimeout'] = request.visibility_timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetQueueAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetQueueAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_queue_attributes_with_options_async(
        self,
        tmp_req: main_models.SetQueueAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetQueueAttributesResponse:
        tmp_req.validate()
        request = main_models.SetQueueAttributesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dlq_policy):
            request.dlq_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        if not DaraCore.is_null(tmp_req.tenant_rate_limit_policy):
            request.tenant_rate_limit_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_rate_limit_policy, 'TenantRateLimitPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.delay_seconds):
            query['DelaySeconds'] = request.delay_seconds
        if not DaraCore.is_null(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not DaraCore.is_null(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not DaraCore.is_null(request.enable_sse):
            query['EnableSSE'] = request.enable_sse
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.maximum_message_size):
            query['MaximumMessageSize'] = request.maximum_message_size
        if not DaraCore.is_null(request.message_retention_period):
            query['MessageRetentionPeriod'] = request.message_retention_period
        if not DaraCore.is_null(request.polling_wait_seconds):
            query['PollingWaitSeconds'] = request.polling_wait_seconds
        if not DaraCore.is_null(request.queue_name):
            query['QueueName'] = request.queue_name
        if not DaraCore.is_null(request.sse_algorithm):
            query['SseAlgorithm'] = request.sse_algorithm
        if not DaraCore.is_null(request.sse_type):
            query['SseType'] = request.sse_type
        if not DaraCore.is_null(request.tenant_rate_limit_policy_shrink):
            query['TenantRateLimitPolicy'] = request.tenant_rate_limit_policy_shrink
        if not DaraCore.is_null(request.visibility_timeout):
            query['VisibilityTimeout'] = request.visibility_timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetQueueAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetQueueAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_queue_attributes(
        self,
        request: main_models.SetQueueAttributesRequest,
    ) -> main_models.SetQueueAttributesResponse:
        runtime = RuntimeOptions()
        return self.set_queue_attributes_with_options(request, runtime)

    async def set_queue_attributes_async(
        self,
        request: main_models.SetQueueAttributesRequest,
    ) -> main_models.SetQueueAttributesResponse:
        runtime = RuntimeOptions()
        return await self.set_queue_attributes_with_options_async(request, runtime)

    def set_subscription_attributes_with_options(
        self,
        tmp_req: main_models.SetSubscriptionAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSubscriptionAttributesResponse:
        tmp_req.validate()
        request = main_models.SetSubscriptionAttributesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dlq_policy):
            request.dlq_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        if not DaraCore.is_null(tmp_req.tenant_rate_limit_policy):
            request.tenant_rate_limit_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_rate_limit_policy, 'TenantRateLimitPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not DaraCore.is_null(request.notify_strategy):
            query['NotifyStrategy'] = request.notify_strategy
        if not DaraCore.is_null(request.sts_role_arn):
            query['StsRoleArn'] = request.sts_role_arn
        if not DaraCore.is_null(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not DaraCore.is_null(request.tenant_rate_limit_policy_shrink):
            query['TenantRateLimitPolicy'] = request.tenant_rate_limit_policy_shrink
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSubscriptionAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSubscriptionAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_subscription_attributes_with_options_async(
        self,
        tmp_req: main_models.SetSubscriptionAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSubscriptionAttributesResponse:
        tmp_req.validate()
        request = main_models.SetSubscriptionAttributesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dlq_policy):
            request.dlq_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        if not DaraCore.is_null(tmp_req.tenant_rate_limit_policy):
            request.tenant_rate_limit_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_rate_limit_policy, 'TenantRateLimitPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not DaraCore.is_null(request.notify_strategy):
            query['NotifyStrategy'] = request.notify_strategy
        if not DaraCore.is_null(request.sts_role_arn):
            query['StsRoleArn'] = request.sts_role_arn
        if not DaraCore.is_null(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not DaraCore.is_null(request.tenant_rate_limit_policy_shrink):
            query['TenantRateLimitPolicy'] = request.tenant_rate_limit_policy_shrink
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSubscriptionAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSubscriptionAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_subscription_attributes(
        self,
        request: main_models.SetSubscriptionAttributesRequest,
    ) -> main_models.SetSubscriptionAttributesResponse:
        runtime = RuntimeOptions()
        return self.set_subscription_attributes_with_options(request, runtime)

    async def set_subscription_attributes_async(
        self,
        request: main_models.SetSubscriptionAttributesRequest,
    ) -> main_models.SetSubscriptionAttributesResponse:
        runtime = RuntimeOptions()
        return await self.set_subscription_attributes_with_options_async(request, runtime)

    def set_topic_attributes_with_options(
        self,
        request: main_models.SetTopicAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTopicAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not DaraCore.is_null(request.enable_sse):
            query['EnableSSE'] = request.enable_sse
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.max_message_size):
            query['MaxMessageSize'] = request.max_message_size
        if not DaraCore.is_null(request.sse_algorithm):
            query['SseAlgorithm'] = request.sse_algorithm
        if not DaraCore.is_null(request.sse_type):
            query['SseType'] = request.sse_type
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTopicAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTopicAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_topic_attributes_with_options_async(
        self,
        request: main_models.SetTopicAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTopicAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not DaraCore.is_null(request.enable_sse):
            query['EnableSSE'] = request.enable_sse
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.max_message_size):
            query['MaxMessageSize'] = request.max_message_size
        if not DaraCore.is_null(request.sse_algorithm):
            query['SseAlgorithm'] = request.sse_algorithm
        if not DaraCore.is_null(request.sse_type):
            query['SseType'] = request.sse_type
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTopicAttributes',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTopicAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_topic_attributes(
        self,
        request: main_models.SetTopicAttributesRequest,
    ) -> main_models.SetTopicAttributesResponse:
        runtime = RuntimeOptions()
        return self.set_topic_attributes_with_options(request, runtime)

    async def set_topic_attributes_async(
        self,
        request: main_models.SetTopicAttributesRequest,
    ) -> main_models.SetTopicAttributesResponse:
        runtime = RuntimeOptions()
        return await self.set_topic_attributes_with_options_async(request, runtime)

    def subscribe_with_options(
        self,
        tmp_req: main_models.SubscribeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubscribeResponse:
        tmp_req.validate()
        request = main_models.SubscribeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dlq_policy):
            request.dlq_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        if not DaraCore.is_null(tmp_req.dm_attributes):
            request.dm_attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.dm_attributes, 'DmAttributes', 'json')
        if not DaraCore.is_null(tmp_req.dysms_attributes):
            request.dysms_attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.dysms_attributes, 'DysmsAttributes', 'json')
        if not DaraCore.is_null(tmp_req.kafka_attributes):
            request.kafka_attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.kafka_attributes, 'KafkaAttributes', 'json')
        if not DaraCore.is_null(tmp_req.tenant_rate_limit_policy):
            request.tenant_rate_limit_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_rate_limit_policy, 'TenantRateLimitPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not DaraCore.is_null(request.dm_attributes_shrink):
            query['DmAttributes'] = request.dm_attributes_shrink
        if not DaraCore.is_null(request.dysms_attributes_shrink):
            query['DysmsAttributes'] = request.dysms_attributes_shrink
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.kafka_attributes_shrink):
            query['KafkaAttributes'] = request.kafka_attributes_shrink
        if not DaraCore.is_null(request.message_tag):
            query['MessageTag'] = request.message_tag
        if not DaraCore.is_null(request.notify_content_format):
            query['NotifyContentFormat'] = request.notify_content_format
        if not DaraCore.is_null(request.notify_strategy):
            query['NotifyStrategy'] = request.notify_strategy
        if not DaraCore.is_null(request.push_type):
            query['PushType'] = request.push_type
        if not DaraCore.is_null(request.sts_role_arn):
            query['StsRoleArn'] = request.sts_role_arn
        if not DaraCore.is_null(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not DaraCore.is_null(request.tenant_rate_limit_policy_shrink):
            query['TenantRateLimitPolicy'] = request.tenant_rate_limit_policy_shrink
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Subscribe',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def subscribe_with_options_async(
        self,
        tmp_req: main_models.SubscribeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubscribeResponse:
        tmp_req.validate()
        request = main_models.SubscribeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dlq_policy):
            request.dlq_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        if not DaraCore.is_null(tmp_req.dm_attributes):
            request.dm_attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.dm_attributes, 'DmAttributes', 'json')
        if not DaraCore.is_null(tmp_req.dysms_attributes):
            request.dysms_attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.dysms_attributes, 'DysmsAttributes', 'json')
        if not DaraCore.is_null(tmp_req.kafka_attributes):
            request.kafka_attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.kafka_attributes, 'KafkaAttributes', 'json')
        if not DaraCore.is_null(tmp_req.tenant_rate_limit_policy):
            request.tenant_rate_limit_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.tenant_rate_limit_policy, 'TenantRateLimitPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not DaraCore.is_null(request.dm_attributes_shrink):
            query['DmAttributes'] = request.dm_attributes_shrink
        if not DaraCore.is_null(request.dysms_attributes_shrink):
            query['DysmsAttributes'] = request.dysms_attributes_shrink
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.kafka_attributes_shrink):
            query['KafkaAttributes'] = request.kafka_attributes_shrink
        if not DaraCore.is_null(request.message_tag):
            query['MessageTag'] = request.message_tag
        if not DaraCore.is_null(request.notify_content_format):
            query['NotifyContentFormat'] = request.notify_content_format
        if not DaraCore.is_null(request.notify_strategy):
            query['NotifyStrategy'] = request.notify_strategy
        if not DaraCore.is_null(request.push_type):
            query['PushType'] = request.push_type
        if not DaraCore.is_null(request.sts_role_arn):
            query['StsRoleArn'] = request.sts_role_arn
        if not DaraCore.is_null(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not DaraCore.is_null(request.tenant_rate_limit_policy_shrink):
            query['TenantRateLimitPolicy'] = request.tenant_rate_limit_policy_shrink
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Subscribe',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def subscribe(
        self,
        request: main_models.SubscribeRequest,
    ) -> main_models.SubscribeResponse:
        runtime = RuntimeOptions()
        return self.subscribe_with_options(request, runtime)

    async def subscribe_async(
        self,
        request: main_models.SubscribeRequest,
    ) -> main_models.SubscribeResponse:
        runtime = RuntimeOptions()
        return await self.subscribe_with_options_async(request, runtime)

    def unsubscribe_with_options(
        self,
        request: main_models.UnsubscribeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnsubscribeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Unsubscribe',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnsubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def unsubscribe_with_options_async(
        self,
        request: main_models.UnsubscribeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnsubscribeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not DaraCore.is_null(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Unsubscribe',
            version = '2022-01-19',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnsubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unsubscribe(
        self,
        request: main_models.UnsubscribeRequest,
    ) -> main_models.UnsubscribeResponse:
        runtime = RuntimeOptions()
        return self.unsubscribe_with_options(request, runtime)

    async def unsubscribe_async(
        self,
        request: main_models.UnsubscribeRequest,
    ) -> main_models.UnsubscribeResponse:
        runtime = RuntimeOptions()
        return await self.unsubscribe_with_options_async(request, runtime)
