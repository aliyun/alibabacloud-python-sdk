# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mns_open20220119 import models as mns_open_20220119_models
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
        self._endpoint_rule = 'regional'
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def authorize_endpoint_acl_with_options(
        self,
        tmp_req: mns_open_20220119_models.AuthorizeEndpointAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.AuthorizeEndpointAclResponse:
        """
        @summary You can call this operation to add one or more rules of access control lists (ACLs) for the endpoint of a type.
        
        @param tmp_req: AuthorizeEndpointAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeEndpointAclResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.AuthorizeEndpointAclShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cidr_list):
            request.cidr_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cidr_list, 'CidrList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.acl_strategy):
            query['AclStrategy'] = request.acl_strategy
        if not UtilClient.is_unset(request.cidr_list_shrink):
            query['CidrList'] = request.cidr_list_shrink
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeEndpointAcl',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.AuthorizeEndpointAclResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.AuthorizeEndpointAclResponse(),
                self.execute(params, req, runtime)
            )

    async def authorize_endpoint_acl_with_options_async(
        self,
        tmp_req: mns_open_20220119_models.AuthorizeEndpointAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.AuthorizeEndpointAclResponse:
        """
        @summary You can call this operation to add one or more rules of access control lists (ACLs) for the endpoint of a type.
        
        @param tmp_req: AuthorizeEndpointAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AuthorizeEndpointAclResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.AuthorizeEndpointAclShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cidr_list):
            request.cidr_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cidr_list, 'CidrList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.acl_strategy):
            query['AclStrategy'] = request.acl_strategy
        if not UtilClient.is_unset(request.cidr_list_shrink):
            query['CidrList'] = request.cidr_list_shrink
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuthorizeEndpointAcl',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.AuthorizeEndpointAclResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.AuthorizeEndpointAclResponse(),
                await self.execute_async(params, req, runtime)
            )

    def authorize_endpoint_acl(
        self,
        request: mns_open_20220119_models.AuthorizeEndpointAclRequest,
    ) -> mns_open_20220119_models.AuthorizeEndpointAclResponse:
        """
        @summary You can call this operation to add one or more rules of access control lists (ACLs) for the endpoint of a type.
        
        @param request: AuthorizeEndpointAclRequest
        @return: AuthorizeEndpointAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.authorize_endpoint_acl_with_options(request, runtime)

    async def authorize_endpoint_acl_async(
        self,
        request: mns_open_20220119_models.AuthorizeEndpointAclRequest,
    ) -> mns_open_20220119_models.AuthorizeEndpointAclResponse:
        """
        @summary You can call this operation to add one or more rules of access control lists (ACLs) for the endpoint of a type.
        
        @param request: AuthorizeEndpointAclRequest
        @return: AuthorizeEndpointAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.authorize_endpoint_acl_with_options_async(request, runtime)

    def create_event_rule_with_options(
        self,
        tmp_req: mns_open_20220119_models.CreateEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.CreateEventRuleResponse:
        """
        @summary 创建事件规则
        
        @param tmp_req: CreateEventRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.CreateEventRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.endpoints):
            request.endpoints_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.endpoints, 'Endpoints', 'json')
        if not UtilClient.is_unset(tmp_req.event_types):
            request.event_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_types, 'EventTypes', 'json')
        if not UtilClient.is_unset(tmp_req.match_rules):
            request.match_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.match_rules, 'MatchRules', 'json')
        query = {}
        if not UtilClient.is_unset(request.endpoints_shrink):
            query['Endpoints'] = request.endpoints_shrink
        if not UtilClient.is_unset(request.event_types_shrink):
            query['EventTypes'] = request.event_types_shrink
        if not UtilClient.is_unset(request.match_rules_shrink):
            query['MatchRules'] = request.match_rules_shrink
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEventRule',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.CreateEventRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.CreateEventRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def create_event_rule_with_options_async(
        self,
        tmp_req: mns_open_20220119_models.CreateEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.CreateEventRuleResponse:
        """
        @summary 创建事件规则
        
        @param tmp_req: CreateEventRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEventRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.CreateEventRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.endpoints):
            request.endpoints_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.endpoints, 'Endpoints', 'json')
        if not UtilClient.is_unset(tmp_req.event_types):
            request.event_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.event_types, 'EventTypes', 'json')
        if not UtilClient.is_unset(tmp_req.match_rules):
            request.match_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.match_rules, 'MatchRules', 'json')
        query = {}
        if not UtilClient.is_unset(request.endpoints_shrink):
            query['Endpoints'] = request.endpoints_shrink
        if not UtilClient.is_unset(request.event_types_shrink):
            query['EventTypes'] = request.event_types_shrink
        if not UtilClient.is_unset(request.match_rules_shrink):
            query['MatchRules'] = request.match_rules_shrink
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEventRule',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.CreateEventRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.CreateEventRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_event_rule(
        self,
        request: mns_open_20220119_models.CreateEventRuleRequest,
    ) -> mns_open_20220119_models.CreateEventRuleResponse:
        """
        @summary 创建事件规则
        
        @param request: CreateEventRuleRequest
        @return: CreateEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_event_rule_with_options(request, runtime)

    async def create_event_rule_async(
        self,
        request: mns_open_20220119_models.CreateEventRuleRequest,
    ) -> mns_open_20220119_models.CreateEventRuleResponse:
        """
        @summary 创建事件规则
        
        @param request: CreateEventRuleRequest
        @return: CreateEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_event_rule_with_options_async(request, runtime)

    def create_queue_with_options(
        self,
        tmp_req: mns_open_20220119_models.CreateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.CreateQueueResponse:
        """
        @summary Creates a queue.
        
        @param tmp_req: CreateQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.CreateQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dlq_policy):
            request.dlq_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.delay_seconds):
            query['DelaySeconds'] = request.delay_seconds
        if not UtilClient.is_unset(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not UtilClient.is_unset(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.maximum_message_size):
            query['MaximumMessageSize'] = request.maximum_message_size
        if not UtilClient.is_unset(request.message_retention_period):
            query['MessageRetentionPeriod'] = request.message_retention_period
        if not UtilClient.is_unset(request.polling_wait_seconds):
            query['PollingWaitSeconds'] = request.polling_wait_seconds
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.visibility_timeout):
            query['VisibilityTimeout'] = request.visibility_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueue',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.CreateQueueResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.CreateQueueResponse(),
                self.execute(params, req, runtime)
            )

    async def create_queue_with_options_async(
        self,
        tmp_req: mns_open_20220119_models.CreateQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.CreateQueueResponse:
        """
        @summary Creates a queue.
        
        @param tmp_req: CreateQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQueueResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.CreateQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dlq_policy):
            request.dlq_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.delay_seconds):
            query['DelaySeconds'] = request.delay_seconds
        if not UtilClient.is_unset(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not UtilClient.is_unset(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.maximum_message_size):
            query['MaximumMessageSize'] = request.maximum_message_size
        if not UtilClient.is_unset(request.message_retention_period):
            query['MessageRetentionPeriod'] = request.message_retention_period
        if not UtilClient.is_unset(request.polling_wait_seconds):
            query['PollingWaitSeconds'] = request.polling_wait_seconds
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.visibility_timeout):
            query['VisibilityTimeout'] = request.visibility_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQueue',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.CreateQueueResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.CreateQueueResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_queue(
        self,
        request: mns_open_20220119_models.CreateQueueRequest,
    ) -> mns_open_20220119_models.CreateQueueResponse:
        """
        @summary Creates a queue.
        
        @param request: CreateQueueRequest
        @return: CreateQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_queue_with_options(request, runtime)

    async def create_queue_async(
        self,
        request: mns_open_20220119_models.CreateQueueRequest,
    ) -> mns_open_20220119_models.CreateQueueResponse:
        """
        @summary Creates a queue.
        
        @param request: CreateQueueRequest
        @return: CreateQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_queue_with_options_async(request, runtime)

    def create_topic_with_options(
        self,
        request: mns_open_20220119_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.CreateTopicResponse:
        """
        @summary Creates a topic.
        
        @param request: CreateTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.enable_logging):
            body['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.max_message_size):
            body['MaxMessageSize'] = request.max_message_size
        if not UtilClient.is_unset(request.topic_name):
            body['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.CreateTopicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.CreateTopicResponse(),
                self.execute(params, req, runtime)
            )

    async def create_topic_with_options_async(
        self,
        request: mns_open_20220119_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.CreateTopicResponse:
        """
        @summary Creates a topic.
        
        @param request: CreateTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.enable_logging):
            body['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.max_message_size):
            body['MaxMessageSize'] = request.max_message_size
        if not UtilClient.is_unset(request.topic_name):
            body['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.CreateTopicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.CreateTopicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_topic(
        self,
        request: mns_open_20220119_models.CreateTopicRequest,
    ) -> mns_open_20220119_models.CreateTopicResponse:
        """
        @summary Creates a topic.
        
        @param request: CreateTopicRequest
        @return: CreateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    async def create_topic_async(
        self,
        request: mns_open_20220119_models.CreateTopicRequest,
    ) -> mns_open_20220119_models.CreateTopicResponse:
        """
        @summary Creates a topic.
        
        @param request: CreateTopicRequest
        @return: CreateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_topic_with_options_async(request, runtime)

    def delete_event_rule_with_options(
        self,
        request: mns_open_20220119_models.DeleteEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.DeleteEventRuleResponse:
        """
        @summary 删除事件规则
        
        @param request: DeleteEventRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRule',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteEventRuleResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteEventRuleResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_event_rule_with_options_async(
        self,
        request: mns_open_20220119_models.DeleteEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.DeleteEventRuleResponse:
        """
        @summary 删除事件规则
        
        @param request: DeleteEventRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEventRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRule',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteEventRuleResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteEventRuleResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_event_rule(
        self,
        request: mns_open_20220119_models.DeleteEventRuleRequest,
    ) -> mns_open_20220119_models.DeleteEventRuleResponse:
        """
        @summary 删除事件规则
        
        @param request: DeleteEventRuleRequest
        @return: DeleteEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_event_rule_with_options(request, runtime)

    async def delete_event_rule_async(
        self,
        request: mns_open_20220119_models.DeleteEventRuleRequest,
    ) -> mns_open_20220119_models.DeleteEventRuleResponse:
        """
        @summary 删除事件规则
        
        @param request: DeleteEventRuleRequest
        @return: DeleteEventRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_rule_with_options_async(request, runtime)

    def delete_queue_with_options(
        self,
        request: mns_open_20220119_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.DeleteQueueResponse:
        """
        @summary Deletes a queue.
        
        @param request: DeleteQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteQueueResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteQueueResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_queue_with_options_async(
        self,
        request: mns_open_20220119_models.DeleteQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.DeleteQueueResponse:
        """
        @summary Deletes a queue.
        
        @param request: DeleteQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQueue',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteQueueResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteQueueResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_queue(
        self,
        request: mns_open_20220119_models.DeleteQueueRequest,
    ) -> mns_open_20220119_models.DeleteQueueResponse:
        """
        @summary Deletes a queue.
        
        @param request: DeleteQueueRequest
        @return: DeleteQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_queue_with_options(request, runtime)

    async def delete_queue_async(
        self,
        request: mns_open_20220119_models.DeleteQueueRequest,
    ) -> mns_open_20220119_models.DeleteQueueResponse:
        """
        @summary Deletes a queue.
        
        @param request: DeleteQueueRequest
        @return: DeleteQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_queue_with_options_async(request, runtime)

    def delete_topic_with_options(
        self,
        request: mns_open_20220119_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.DeleteTopicResponse:
        """
        @summary Deletes a topic.
        
        @param request: DeleteTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteTopicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteTopicResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_topic_with_options_async(
        self,
        request: mns_open_20220119_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.DeleteTopicResponse:
        """
        @summary Deletes a topic.
        
        @param request: DeleteTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteTopicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.DeleteTopicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_topic(
        self,
        request: mns_open_20220119_models.DeleteTopicRequest,
    ) -> mns_open_20220119_models.DeleteTopicResponse:
        """
        @summary Deletes a topic.
        
        @param request: DeleteTopicRequest
        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    async def delete_topic_async(
        self,
        request: mns_open_20220119_models.DeleteTopicRequest,
    ) -> mns_open_20220119_models.DeleteTopicResponse:
        """
        @summary Deletes a topic.
        
        @param request: DeleteTopicRequest
        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_topic_with_options_async(request, runtime)

    def disable_endpoint_with_options(
        self,
        request: mns_open_20220119_models.DisableEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.DisableEndpointResponse:
        """
        @summary You can call this operation to disenable the endpoint of a type. After the endpoint is disabled, all requests from the endpoint are blocked and an error is returned.
        
        @param request: DisableEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableEndpoint',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.DisableEndpointResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.DisableEndpointResponse(),
                self.execute(params, req, runtime)
            )

    async def disable_endpoint_with_options_async(
        self,
        request: mns_open_20220119_models.DisableEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.DisableEndpointResponse:
        """
        @summary You can call this operation to disenable the endpoint of a type. After the endpoint is disabled, all requests from the endpoint are blocked and an error is returned.
        
        @param request: DisableEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableEndpoint',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.DisableEndpointResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.DisableEndpointResponse(),
                await self.execute_async(params, req, runtime)
            )

    def disable_endpoint(
        self,
        request: mns_open_20220119_models.DisableEndpointRequest,
    ) -> mns_open_20220119_models.DisableEndpointResponse:
        """
        @summary You can call this operation to disenable the endpoint of a type. After the endpoint is disabled, all requests from the endpoint are blocked and an error is returned.
        
        @param request: DisableEndpointRequest
        @return: DisableEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_endpoint_with_options(request, runtime)

    async def disable_endpoint_async(
        self,
        request: mns_open_20220119_models.DisableEndpointRequest,
    ) -> mns_open_20220119_models.DisableEndpointResponse:
        """
        @summary You can call this operation to disenable the endpoint of a type. After the endpoint is disabled, all requests from the endpoint are blocked and an error is returned.
        
        @param request: DisableEndpointRequest
        @return: DisableEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_endpoint_with_options_async(request, runtime)

    def enable_endpoint_with_options(
        self,
        request: mns_open_20220119_models.EnableEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.EnableEndpointResponse:
        """
        @summary You can call this operation to enable the endpoint of a type. If the endpoint is enabled, requests from the endpoint that are included in the access control lists (ACLs) are not blocked.
        
        @param request: EnableEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableEndpoint',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.EnableEndpointResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.EnableEndpointResponse(),
                self.execute(params, req, runtime)
            )

    async def enable_endpoint_with_options_async(
        self,
        request: mns_open_20220119_models.EnableEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.EnableEndpointResponse:
        """
        @summary You can call this operation to enable the endpoint of a type. If the endpoint is enabled, requests from the endpoint that are included in the access control lists (ACLs) are not blocked.
        
        @param request: EnableEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableEndpoint',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.EnableEndpointResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.EnableEndpointResponse(),
                await self.execute_async(params, req, runtime)
            )

    def enable_endpoint(
        self,
        request: mns_open_20220119_models.EnableEndpointRequest,
    ) -> mns_open_20220119_models.EnableEndpointResponse:
        """
        @summary You can call this operation to enable the endpoint of a type. If the endpoint is enabled, requests from the endpoint that are included in the access control lists (ACLs) are not blocked.
        
        @param request: EnableEndpointRequest
        @return: EnableEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_endpoint_with_options(request, runtime)

    async def enable_endpoint_async(
        self,
        request: mns_open_20220119_models.EnableEndpointRequest,
    ) -> mns_open_20220119_models.EnableEndpointResponse:
        """
        @summary You can call this operation to enable the endpoint of a type. If the endpoint is enabled, requests from the endpoint that are included in the access control lists (ACLs) are not blocked.
        
        @param request: EnableEndpointRequest
        @return: EnableEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_endpoint_with_options_async(request, runtime)

    def get_endpoint_attribute_with_options(
        self,
        request: mns_open_20220119_models.GetEndpointAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.GetEndpointAttributeResponse:
        """
        @summary GetEndpointAttribute
        
        @param request: GetEndpointAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEndpointAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEndpointAttribute',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.GetEndpointAttributeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.GetEndpointAttributeResponse(),
                self.execute(params, req, runtime)
            )

    async def get_endpoint_attribute_with_options_async(
        self,
        request: mns_open_20220119_models.GetEndpointAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.GetEndpointAttributeResponse:
        """
        @summary GetEndpointAttribute
        
        @param request: GetEndpointAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEndpointAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEndpointAttribute',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.GetEndpointAttributeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.GetEndpointAttributeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_endpoint_attribute(
        self,
        request: mns_open_20220119_models.GetEndpointAttributeRequest,
    ) -> mns_open_20220119_models.GetEndpointAttributeResponse:
        """
        @summary GetEndpointAttribute
        
        @param request: GetEndpointAttributeRequest
        @return: GetEndpointAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_endpoint_attribute_with_options(request, runtime)

    async def get_endpoint_attribute_async(
        self,
        request: mns_open_20220119_models.GetEndpointAttributeRequest,
    ) -> mns_open_20220119_models.GetEndpointAttributeResponse:
        """
        @summary GetEndpointAttribute
        
        @param request: GetEndpointAttributeRequest
        @return: GetEndpointAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_endpoint_attribute_with_options_async(request, runtime)

    def get_queue_attributes_with_options(
        self,
        request: mns_open_20220119_models.GetQueueAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.GetQueueAttributesResponse:
        """
        @summary Queries the attributes of an existing queue.
        
        @param request: GetQueueAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.GetQueueAttributesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.GetQueueAttributesResponse(),
                self.execute(params, req, runtime)
            )

    async def get_queue_attributes_with_options_async(
        self,
        request: mns_open_20220119_models.GetQueueAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.GetQueueAttributesResponse:
        """
        @summary Queries the attributes of an existing queue.
        
        @param request: GetQueueAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQueueAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQueueAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.GetQueueAttributesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.GetQueueAttributesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_queue_attributes(
        self,
        request: mns_open_20220119_models.GetQueueAttributesRequest,
    ) -> mns_open_20220119_models.GetQueueAttributesResponse:
        """
        @summary Queries the attributes of an existing queue.
        
        @param request: GetQueueAttributesRequest
        @return: GetQueueAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_queue_attributes_with_options(request, runtime)

    async def get_queue_attributes_async(
        self,
        request: mns_open_20220119_models.GetQueueAttributesRequest,
    ) -> mns_open_20220119_models.GetQueueAttributesResponse:
        """
        @summary Queries the attributes of an existing queue.
        
        @param request: GetQueueAttributesRequest
        @return: GetQueueAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_attributes_with_options_async(request, runtime)

    def get_subscription_attributes_with_options(
        self,
        request: mns_open_20220119_models.GetSubscriptionAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.GetSubscriptionAttributesResponse:
        """
        @summary Queries the attributes of a subscription.
        
        @param request: GetSubscriptionAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubscriptionAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.GetSubscriptionAttributesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.GetSubscriptionAttributesResponse(),
                self.execute(params, req, runtime)
            )

    async def get_subscription_attributes_with_options_async(
        self,
        request: mns_open_20220119_models.GetSubscriptionAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.GetSubscriptionAttributesResponse:
        """
        @summary Queries the attributes of a subscription.
        
        @param request: GetSubscriptionAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubscriptionAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.GetSubscriptionAttributesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.GetSubscriptionAttributesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_subscription_attributes(
        self,
        request: mns_open_20220119_models.GetSubscriptionAttributesRequest,
    ) -> mns_open_20220119_models.GetSubscriptionAttributesResponse:
        """
        @summary Queries the attributes of a subscription.
        
        @param request: GetSubscriptionAttributesRequest
        @return: GetSubscriptionAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_subscription_attributes_with_options(request, runtime)

    async def get_subscription_attributes_async(
        self,
        request: mns_open_20220119_models.GetSubscriptionAttributesRequest,
    ) -> mns_open_20220119_models.GetSubscriptionAttributesResponse:
        """
        @summary Queries the attributes of a subscription.
        
        @param request: GetSubscriptionAttributesRequest
        @return: GetSubscriptionAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_subscription_attributes_with_options_async(request, runtime)

    def get_topic_attributes_with_options(
        self,
        request: mns_open_20220119_models.GetTopicAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.GetTopicAttributesResponse:
        """
        @summary Queries the attributes of a topic.
        
        @param request: GetTopicAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.GetTopicAttributesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.GetTopicAttributesResponse(),
                self.execute(params, req, runtime)
            )

    async def get_topic_attributes_with_options_async(
        self,
        request: mns_open_20220119_models.GetTopicAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.GetTopicAttributesResponse:
        """
        @summary Queries the attributes of a topic.
        
        @param request: GetTopicAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.GetTopicAttributesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.GetTopicAttributesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_topic_attributes(
        self,
        request: mns_open_20220119_models.GetTopicAttributesRequest,
    ) -> mns_open_20220119_models.GetTopicAttributesResponse:
        """
        @summary Queries the attributes of a topic.
        
        @param request: GetTopicAttributesRequest
        @return: GetTopicAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_attributes_with_options(request, runtime)

    async def get_topic_attributes_async(
        self,
        request: mns_open_20220119_models.GetTopicAttributesRequest,
    ) -> mns_open_20220119_models.GetTopicAttributesResponse:
        """
        @summary Queries the attributes of a topic.
        
        @param request: GetTopicAttributesRequest
        @return: GetTopicAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_attributes_with_options_async(request, runtime)

    def list_queue_with_options(
        self,
        request: mns_open_20220119_models.ListQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.ListQueueResponse:
        """
        @summary Queries all queues that belong to an Alibaba Cloud account. The queues are displayed by page.
        
        @param request: ListQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueue',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.ListQueueResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.ListQueueResponse(),
                self.execute(params, req, runtime)
            )

    async def list_queue_with_options_async(
        self,
        request: mns_open_20220119_models.ListQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.ListQueueResponse:
        """
        @summary Queries all queues that belong to an Alibaba Cloud account. The queues are displayed by page.
        
        @param request: ListQueueRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueue',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.ListQueueResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.ListQueueResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_queue(
        self,
        request: mns_open_20220119_models.ListQueueRequest,
    ) -> mns_open_20220119_models.ListQueueResponse:
        """
        @summary Queries all queues that belong to an Alibaba Cloud account. The queues are displayed by page.
        
        @param request: ListQueueRequest
        @return: ListQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_queue_with_options(request, runtime)

    async def list_queue_async(
        self,
        request: mns_open_20220119_models.ListQueueRequest,
    ) -> mns_open_20220119_models.ListQueueResponse:
        """
        @summary Queries all queues that belong to an Alibaba Cloud account. The queues are displayed by page.
        
        @param request: ListQueueRequest
        @return: ListQueueResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_queue_with_options_async(request, runtime)

    def list_subscription_by_topic_with_options(
        self,
        request: mns_open_20220119_models.ListSubscriptionByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.ListSubscriptionByTopicResponse:
        """
        @summary Queries all subscriptions to a topic. The subscriptions are displayed by page.
        
        @param request: ListSubscriptionByTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubscriptionByTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubscriptionByTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.ListSubscriptionByTopicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.ListSubscriptionByTopicResponse(),
                self.execute(params, req, runtime)
            )

    async def list_subscription_by_topic_with_options_async(
        self,
        request: mns_open_20220119_models.ListSubscriptionByTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.ListSubscriptionByTopicResponse:
        """
        @summary Queries all subscriptions to a topic. The subscriptions are displayed by page.
        
        @param request: ListSubscriptionByTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSubscriptionByTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSubscriptionByTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.ListSubscriptionByTopicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.ListSubscriptionByTopicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_subscription_by_topic(
        self,
        request: mns_open_20220119_models.ListSubscriptionByTopicRequest,
    ) -> mns_open_20220119_models.ListSubscriptionByTopicResponse:
        """
        @summary Queries all subscriptions to a topic. The subscriptions are displayed by page.
        
        @param request: ListSubscriptionByTopicRequest
        @return: ListSubscriptionByTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_subscription_by_topic_with_options(request, runtime)

    async def list_subscription_by_topic_async(
        self,
        request: mns_open_20220119_models.ListSubscriptionByTopicRequest,
    ) -> mns_open_20220119_models.ListSubscriptionByTopicResponse:
        """
        @summary Queries all subscriptions to a topic. The subscriptions are displayed by page.
        
        @param request: ListSubscriptionByTopicRequest
        @return: ListSubscriptionByTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_subscription_by_topic_with_options_async(request, runtime)

    def list_topic_with_options(
        self,
        request: mns_open_20220119_models.ListTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.ListTopicResponse:
        """
        @summary Queries the topics that belong to an Alibaba Cloud account. The topics are displayed by page.
        
        @param request: ListTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.ListTopicResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.ListTopicResponse(),
                self.execute(params, req, runtime)
            )

    async def list_topic_with_options_async(
        self,
        request: mns_open_20220119_models.ListTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.ListTopicResponse:
        """
        @summary Queries the topics that belong to an Alibaba Cloud account. The topics are displayed by page.
        
        @param request: ListTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTopic',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.ListTopicResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.ListTopicResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_topic(
        self,
        request: mns_open_20220119_models.ListTopicRequest,
    ) -> mns_open_20220119_models.ListTopicResponse:
        """
        @summary Queries the topics that belong to an Alibaba Cloud account. The topics are displayed by page.
        
        @param request: ListTopicRequest
        @return: ListTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_topic_with_options(request, runtime)

    async def list_topic_async(
        self,
        request: mns_open_20220119_models.ListTopicRequest,
    ) -> mns_open_20220119_models.ListTopicResponse:
        """
        @summary Queries the topics that belong to an Alibaba Cloud account. The topics are displayed by page.
        
        @param request: ListTopicRequest
        @return: ListTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_topic_with_options_async(request, runtime)

    def revoke_endpoint_acl_with_options(
        self,
        tmp_req: mns_open_20220119_models.RevokeEndpointAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.RevokeEndpointAclResponse:
        """
        @summary You can call this operation to delete one or more rules of access control lists (ACLs) for the endpoint of a type.
        
        @param tmp_req: RevokeEndpointAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeEndpointAclResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.RevokeEndpointAclShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cidr_list):
            request.cidr_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cidr_list, 'CidrList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.acl_strategy):
            query['AclStrategy'] = request.acl_strategy
        if not UtilClient.is_unset(request.cidr_list_shrink):
            query['CidrList'] = request.cidr_list_shrink
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeEndpointAcl',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.RevokeEndpointAclResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.RevokeEndpointAclResponse(),
                self.execute(params, req, runtime)
            )

    async def revoke_endpoint_acl_with_options_async(
        self,
        tmp_req: mns_open_20220119_models.RevokeEndpointAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.RevokeEndpointAclResponse:
        """
        @summary You can call this operation to delete one or more rules of access control lists (ACLs) for the endpoint of a type.
        
        @param tmp_req: RevokeEndpointAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeEndpointAclResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.RevokeEndpointAclShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cidr_list):
            request.cidr_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cidr_list, 'CidrList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.acl_strategy):
            query['AclStrategy'] = request.acl_strategy
        if not UtilClient.is_unset(request.cidr_list_shrink):
            query['CidrList'] = request.cidr_list_shrink
        if not UtilClient.is_unset(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeEndpointAcl',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.RevokeEndpointAclResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.RevokeEndpointAclResponse(),
                await self.execute_async(params, req, runtime)
            )

    def revoke_endpoint_acl(
        self,
        request: mns_open_20220119_models.RevokeEndpointAclRequest,
    ) -> mns_open_20220119_models.RevokeEndpointAclResponse:
        """
        @summary You can call this operation to delete one or more rules of access control lists (ACLs) for the endpoint of a type.
        
        @param request: RevokeEndpointAclRequest
        @return: RevokeEndpointAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_endpoint_acl_with_options(request, runtime)

    async def revoke_endpoint_acl_async(
        self,
        request: mns_open_20220119_models.RevokeEndpointAclRequest,
    ) -> mns_open_20220119_models.RevokeEndpointAclResponse:
        """
        @summary You can call this operation to delete one or more rules of access control lists (ACLs) for the endpoint of a type.
        
        @param request: RevokeEndpointAclRequest
        @return: RevokeEndpointAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_endpoint_acl_with_options_async(request, runtime)

    def set_queue_attributes_with_options(
        self,
        tmp_req: mns_open_20220119_models.SetQueueAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.SetQueueAttributesResponse:
        """
        @summary Modifies a queue.
        
        @param tmp_req: SetQueueAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetQueueAttributesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.SetQueueAttributesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dlq_policy):
            request.dlq_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.delay_seconds):
            query['DelaySeconds'] = request.delay_seconds
        if not UtilClient.is_unset(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not UtilClient.is_unset(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.maximum_message_size):
            query['MaximumMessageSize'] = request.maximum_message_size
        if not UtilClient.is_unset(request.message_retention_period):
            query['MessageRetentionPeriod'] = request.message_retention_period
        if not UtilClient.is_unset(request.polling_wait_seconds):
            query['PollingWaitSeconds'] = request.polling_wait_seconds
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.visibility_timeout):
            query['VisibilityTimeout'] = request.visibility_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetQueueAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.SetQueueAttributesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.SetQueueAttributesResponse(),
                self.execute(params, req, runtime)
            )

    async def set_queue_attributes_with_options_async(
        self,
        tmp_req: mns_open_20220119_models.SetQueueAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.SetQueueAttributesResponse:
        """
        @summary Modifies a queue.
        
        @param tmp_req: SetQueueAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetQueueAttributesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.SetQueueAttributesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dlq_policy):
            request.dlq_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.delay_seconds):
            query['DelaySeconds'] = request.delay_seconds
        if not UtilClient.is_unset(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not UtilClient.is_unset(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.maximum_message_size):
            query['MaximumMessageSize'] = request.maximum_message_size
        if not UtilClient.is_unset(request.message_retention_period):
            query['MessageRetentionPeriod'] = request.message_retention_period
        if not UtilClient.is_unset(request.polling_wait_seconds):
            query['PollingWaitSeconds'] = request.polling_wait_seconds
        if not UtilClient.is_unset(request.queue_name):
            query['QueueName'] = request.queue_name
        if not UtilClient.is_unset(request.visibility_timeout):
            query['VisibilityTimeout'] = request.visibility_timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetQueueAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.SetQueueAttributesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.SetQueueAttributesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def set_queue_attributes(
        self,
        request: mns_open_20220119_models.SetQueueAttributesRequest,
    ) -> mns_open_20220119_models.SetQueueAttributesResponse:
        """
        @summary Modifies a queue.
        
        @param request: SetQueueAttributesRequest
        @return: SetQueueAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_queue_attributes_with_options(request, runtime)

    async def set_queue_attributes_async(
        self,
        request: mns_open_20220119_models.SetQueueAttributesRequest,
    ) -> mns_open_20220119_models.SetQueueAttributesResponse:
        """
        @summary Modifies a queue.
        
        @param request: SetQueueAttributesRequest
        @return: SetQueueAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_queue_attributes_with_options_async(request, runtime)

    def set_subscription_attributes_with_options(
        self,
        tmp_req: mns_open_20220119_models.SetSubscriptionAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.SetSubscriptionAttributesResponse:
        """
        @summary Modifies the attributes of a subscription.
        
        @param tmp_req: SetSubscriptionAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSubscriptionAttributesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.SetSubscriptionAttributesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dlq_policy):
            request.dlq_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not UtilClient.is_unset(request.notify_strategy):
            query['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSubscriptionAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.SetSubscriptionAttributesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.SetSubscriptionAttributesResponse(),
                self.execute(params, req, runtime)
            )

    async def set_subscription_attributes_with_options_async(
        self,
        tmp_req: mns_open_20220119_models.SetSubscriptionAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.SetSubscriptionAttributesResponse:
        """
        @summary Modifies the attributes of a subscription.
        
        @param tmp_req: SetSubscriptionAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSubscriptionAttributesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.SetSubscriptionAttributesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dlq_policy):
            request.dlq_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not UtilClient.is_unset(request.notify_strategy):
            query['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSubscriptionAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.SetSubscriptionAttributesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.SetSubscriptionAttributesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def set_subscription_attributes(
        self,
        request: mns_open_20220119_models.SetSubscriptionAttributesRequest,
    ) -> mns_open_20220119_models.SetSubscriptionAttributesResponse:
        """
        @summary Modifies the attributes of a subscription.
        
        @param request: SetSubscriptionAttributesRequest
        @return: SetSubscriptionAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_subscription_attributes_with_options(request, runtime)

    async def set_subscription_attributes_async(
        self,
        request: mns_open_20220119_models.SetSubscriptionAttributesRequest,
    ) -> mns_open_20220119_models.SetSubscriptionAttributesResponse:
        """
        @summary Modifies the attributes of a subscription.
        
        @param request: SetSubscriptionAttributesRequest
        @return: SetSubscriptionAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_subscription_attributes_with_options_async(request, runtime)

    def set_topic_attributes_with_options(
        self,
        request: mns_open_20220119_models.SetTopicAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.SetTopicAttributesResponse:
        """
        @summary Modifies the attributes of a topic.
        
        @param request: SetTopicAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetTopicAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.max_message_size):
            query['MaxMessageSize'] = request.max_message_size
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTopicAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.SetTopicAttributesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.SetTopicAttributesResponse(),
                self.execute(params, req, runtime)
            )

    async def set_topic_attributes_with_options_async(
        self,
        request: mns_open_20220119_models.SetTopicAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.SetTopicAttributesResponse:
        """
        @summary Modifies the attributes of a topic.
        
        @param request: SetTopicAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetTopicAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_logging):
            query['EnableLogging'] = request.enable_logging
        if not UtilClient.is_unset(request.max_message_size):
            query['MaxMessageSize'] = request.max_message_size
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTopicAttributes',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.SetTopicAttributesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.SetTopicAttributesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def set_topic_attributes(
        self,
        request: mns_open_20220119_models.SetTopicAttributesRequest,
    ) -> mns_open_20220119_models.SetTopicAttributesResponse:
        """
        @summary Modifies the attributes of a topic.
        
        @param request: SetTopicAttributesRequest
        @return: SetTopicAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_topic_attributes_with_options(request, runtime)

    async def set_topic_attributes_async(
        self,
        request: mns_open_20220119_models.SetTopicAttributesRequest,
    ) -> mns_open_20220119_models.SetTopicAttributesResponse:
        """
        @summary Modifies the attributes of a topic.
        
        @param request: SetTopicAttributesRequest
        @return: SetTopicAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_topic_attributes_with_options_async(request, runtime)

    def subscribe_with_options(
        self,
        tmp_req: mns_open_20220119_models.SubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.SubscribeResponse:
        """
        @summary Creates a subscription to a topic.
        
        @param tmp_req: SubscribeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubscribeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.SubscribeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dlq_policy):
            request.dlq_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.message_tag):
            query['MessageTag'] = request.message_tag
        if not UtilClient.is_unset(request.notify_content_format):
            query['NotifyContentFormat'] = request.notify_content_format
        if not UtilClient.is_unset(request.notify_strategy):
            query['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Subscribe',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.SubscribeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.SubscribeResponse(),
                self.execute(params, req, runtime)
            )

    async def subscribe_with_options_async(
        self,
        tmp_req: mns_open_20220119_models.SubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.SubscribeResponse:
        """
        @summary Creates a subscription to a topic.
        
        @param tmp_req: SubscribeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubscribeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = mns_open_20220119_models.SubscribeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dlq_policy):
            request.dlq_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dlq_policy, 'DlqPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.dlq_policy_shrink):
            query['DlqPolicy'] = request.dlq_policy_shrink
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.message_tag):
            query['MessageTag'] = request.message_tag
        if not UtilClient.is_unset(request.notify_content_format):
            query['NotifyContentFormat'] = request.notify_content_format
        if not UtilClient.is_unset(request.notify_strategy):
            query['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Subscribe',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.SubscribeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.SubscribeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def subscribe(
        self,
        request: mns_open_20220119_models.SubscribeRequest,
    ) -> mns_open_20220119_models.SubscribeResponse:
        """
        @summary Creates a subscription to a topic.
        
        @param request: SubscribeRequest
        @return: SubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.subscribe_with_options(request, runtime)

    async def subscribe_async(
        self,
        request: mns_open_20220119_models.SubscribeRequest,
    ) -> mns_open_20220119_models.SubscribeResponse:
        """
        @summary Creates a subscription to a topic.
        
        @param request: SubscribeRequest
        @return: SubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.subscribe_with_options_async(request, runtime)

    def unsubscribe_with_options(
        self,
        request: mns_open_20220119_models.UnsubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.UnsubscribeResponse:
        """
        @summary Deletes a subscription.
        
        @param request: UnsubscribeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnsubscribeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Unsubscribe',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.UnsubscribeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.UnsubscribeResponse(),
                self.execute(params, req, runtime)
            )

    async def unsubscribe_with_options_async(
        self,
        request: mns_open_20220119_models.UnsubscribeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mns_open_20220119_models.UnsubscribeResponse:
        """
        @summary Deletes a subscription.
        
        @param request: UnsubscribeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnsubscribeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subscription_name):
            query['SubscriptionName'] = request.subscription_name
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Unsubscribe',
            version='2022-01-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                mns_open_20220119_models.UnsubscribeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                mns_open_20220119_models.UnsubscribeResponse(),
                await self.execute_async(params, req, runtime)
            )

    def unsubscribe(
        self,
        request: mns_open_20220119_models.UnsubscribeRequest,
    ) -> mns_open_20220119_models.UnsubscribeResponse:
        """
        @summary Deletes a subscription.
        
        @param request: UnsubscribeRequest
        @return: UnsubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unsubscribe_with_options(request, runtime)

    async def unsubscribe_async(
        self,
        request: mns_open_20220119_models.UnsubscribeRequest,
    ) -> mns_open_20220119_models.UnsubscribeResponse:
        """
        @summary Deletes a subscription.
        
        @param request: UnsubscribeRequest
        @return: UnsubscribeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unsubscribe_with_options_async(request, runtime)
