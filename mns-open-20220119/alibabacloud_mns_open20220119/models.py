# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class EventMatchRule(TeaModel):
    def __init__(
        self,
        match_state: bool = None,
        name: str = None,
        prefix: str = None,
        suffix: str = None,
    ):
        self.match_state = match_state
        self.name = name
        self.prefix = prefix
        self.suffix = suffix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_state is not None:
            result['MatchState'] = self.match_state
        if self.name is not None:
            result['Name'] = self.name
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.suffix is not None:
            result['Suffix'] = self.suffix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchState') is not None:
            self.match_state = m.get('MatchState')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Suffix') is not None:
            self.suffix = m.get('Suffix')
        return self


class AuthorizeEndpointAclRequest(TeaModel):
    def __init__(
        self,
        acl_strategy: str = None,
        cidr_list: List[str] = None,
        endpoint_type: str = None,
    ):
        # The ACL policy. Valid values:
        # 
        # *   **allow**: indicates that this operation is included in the Cidr whitelist. (Only the allow is supported.)
        # 
        # This parameter is required.
        self.acl_strategy = acl_strategy
        # The list of CIDR block.
        # 
        # This parameter is required.
        self.cidr_list = cidr_list
        # The type of the endpoint. Valid values:
        # 
        # *   **public**: indicates public endpoint. (Only the public endpoint is supported.)
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_strategy is not None:
            result['AclStrategy'] = self.acl_strategy
        if self.cidr_list is not None:
            result['CidrList'] = self.cidr_list
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStrategy') is not None:
            self.acl_strategy = m.get('AclStrategy')
        if m.get('CidrList') is not None:
            self.cidr_list = m.get('CidrList')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        return self


class AuthorizeEndpointAclShrinkRequest(TeaModel):
    def __init__(
        self,
        acl_strategy: str = None,
        cidr_list_shrink: str = None,
        endpoint_type: str = None,
    ):
        # The ACL policy. Valid values:
        # 
        # *   **allow**: indicates that this operation is included in the Cidr whitelist. (Only the allow is supported.)
        # 
        # This parameter is required.
        self.acl_strategy = acl_strategy
        # The list of CIDR block.
        # 
        # This parameter is required.
        self.cidr_list_shrink = cidr_list_shrink
        # The type of the endpoint. Valid values:
        # 
        # *   **public**: indicates public endpoint. (Only the public endpoint is supported.)
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_strategy is not None:
            result['AclStrategy'] = self.acl_strategy
        if self.cidr_list_shrink is not None:
            result['CidrList'] = self.cidr_list_shrink
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStrategy') is not None:
            self.acl_strategy = m.get('AclStrategy')
        if m.get('CidrList') is not None:
            self.cidr_list_shrink = m.get('CidrList')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        return self


class AuthorizeEndpointAclResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthorizeEndpointAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthorizeEndpointAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AuthorizeEndpointAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventRuleRequestEndpoints(TeaModel):
    def __init__(
        self,
        endpoint_type: str = None,
        endpoint_value: str = None,
    ):
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # This parameter is required.
        self.endpoint_value = endpoint_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.endpoint_value is not None:
            result['EndpointValue'] = self.endpoint_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('EndpointValue') is not None:
            self.endpoint_value = m.get('EndpointValue')
        return self


class CreateEventRuleRequest(TeaModel):
    def __init__(
        self,
        endpoints: List[CreateEventRuleRequestEndpoints] = None,
        event_types: List[str] = None,
        match_rules: List[List[EventMatchRule]] = None,
        product_name: str = None,
        rule_name: str = None,
    ):
        # This parameter is required.
        self.endpoints = endpoints
        # This parameter is required.
        self.event_types = event_types
        # This parameter is required.
        self.match_rules = match_rules
        # This parameter is required.
        self.product_name = product_name
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()
        if self.match_rules:
            for k in self.match_rules:
                for k1 in k:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.event_types is not None:
            result['EventTypes'] = self.event_types
        result['MatchRules'] = []
        if self.match_rules is not None:
            for k in self.match_rules:
                l1 = []
                for k1 in k:
                    l1.append(k1.to_map() if k1 else None)
                result['MatchRules'].append(l1)
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = CreateEventRuleRequestEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')
        self.match_rules = []
        if m.get('MatchRules') is not None:
            for k in m.get('MatchRules'):
                l1 = []
                for k1 in k:
                    temp_model = EventMatchRule()
                    l1.append(temp_model.from_map(k1))
                self.match_rules.append(l1)
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class CreateEventRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        endpoints_shrink: str = None,
        event_types_shrink: str = None,
        match_rules_shrink: str = None,
        product_name: str = None,
        rule_name: str = None,
    ):
        # This parameter is required.
        self.endpoints_shrink = endpoints_shrink
        # This parameter is required.
        self.event_types_shrink = event_types_shrink
        # This parameter is required.
        self.match_rules_shrink = match_rules_shrink
        # This parameter is required.
        self.product_name = product_name
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoints_shrink is not None:
            result['Endpoints'] = self.endpoints_shrink
        if self.event_types_shrink is not None:
            result['EventTypes'] = self.event_types_shrink
        if self.match_rules_shrink is not None:
            result['MatchRules'] = self.match_rules_shrink
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoints') is not None:
            self.endpoints_shrink = m.get('Endpoints')
        if m.get('EventTypes') is not None:
            self.event_types_shrink = m.get('EventTypes')
        if m.get('MatchRules') is not None:
            self.match_rules_shrink = m.get('MatchRules')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class CreateEventRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEventRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEventRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQueueRequestDlqPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
        max_receive_count: int = None,
    ):
        # The queue to which dead-letter messages are delivered.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Specifies whether to enable the dead-letter message delivery.
        self.enabled = enabled
        # The maximum number of retries.
        self.max_receive_count = max_receive_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_queue is not None:
            result['DeadLetterTargetQueue'] = self.dead_letter_target_queue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.max_receive_count is not None:
            result['MaxReceiveCount'] = self.max_receive_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('MaxReceiveCount') is not None:
            self.max_receive_count = m.get('MaxReceiveCount')
        return self


class CreateQueueRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateQueueRequest(TeaModel):
    def __init__(
        self,
        delay_seconds: int = None,
        dlq_policy: CreateQueueRequestDlqPolicy = None,
        enable_logging: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        tag: List[CreateQueueRequestTag] = None,
        visibility_timeout: int = None,
    ):
        # The period after which all messages sent to the queue are consumed. Valid values: 0 to 604800. Unit: seconds. Default value: 0
        self.delay_seconds = delay_seconds
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # Specifies whether to enable the log management feature. Valid values:
        # 
        # *   true: enabled.
        # *   false: disabled.
        # 
        # Default value: false.
        self.enable_logging = enable_logging
        # The maximum length of the message that is sent to the queue. Valid values: 1024 to 65536. Unit: bytes. Default value: 65536.
        self.maximum_message_size = maximum_message_size
        # The maximum duration for which a message is retained in the queue. After the specified retention period ends, the message is deleted regardless of whether the message is consumed. Valid values: 60 to 604800. Unit: seconds. Default value: 345600.
        self.message_retention_period = message_retention_period
        # The maximum duration for which long polling requests are held after the ReceiveMessage operation is called. Valid values: 0 to 30. Unit: seconds. Default value: 0
        self.polling_wait_seconds = polling_wait_seconds
        # The name of the queue.
        # 
        # This parameter is required.
        self.queue_name = queue_name
        # The tags.
        self.tag = tag
        # The duration for which a message stays in the Inactive state after the message is received from the queue. Valid values: 1 to 43200. Unit: seconds. Default value: 30.
        self.visibility_timeout = visibility_timeout

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('DlqPolicy') is not None:
            temp_model = CreateQueueRequestDlqPolicy()
            self.dlq_policy = temp_model.from_map(m['DlqPolicy'])
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateQueueRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class CreateQueueShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateQueueShrinkRequest(TeaModel):
    def __init__(
        self,
        delay_seconds: int = None,
        dlq_policy_shrink: str = None,
        enable_logging: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        tag: List[CreateQueueShrinkRequestTag] = None,
        visibility_timeout: int = None,
    ):
        # The period after which all messages sent to the queue are consumed. Valid values: 0 to 604800. Unit: seconds. Default value: 0
        self.delay_seconds = delay_seconds
        # The dead-letter queue policy.
        self.dlq_policy_shrink = dlq_policy_shrink
        # Specifies whether to enable the log management feature. Valid values:
        # 
        # *   true: enabled.
        # *   false: disabled.
        # 
        # Default value: false.
        self.enable_logging = enable_logging
        # The maximum length of the message that is sent to the queue. Valid values: 1024 to 65536. Unit: bytes. Default value: 65536.
        self.maximum_message_size = maximum_message_size
        # The maximum duration for which a message is retained in the queue. After the specified retention period ends, the message is deleted regardless of whether the message is consumed. Valid values: 60 to 604800. Unit: seconds. Default value: 345600.
        self.message_retention_period = message_retention_period
        # The maximum duration for which long polling requests are held after the ReceiveMessage operation is called. Valid values: 0 to 30. Unit: seconds. Default value: 0
        self.polling_wait_seconds = polling_wait_seconds
        # The name of the queue.
        # 
        # This parameter is required.
        self.queue_name = queue_name
        # The tags.
        self.tag = tag
        # The duration for which a message stays in the Inactive state after the message is received from the queue. Valid values: 1 to 43200. Unit: seconds. Default value: 30.
        self.visibility_timeout = visibility_timeout

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.dlq_policy_shrink is not None:
            result['DlqPolicy'] = self.dlq_policy_shrink
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('DlqPolicy') is not None:
            self.dlq_policy_shrink = m.get('DlqPolicy')
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateQueueShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class CreateQueueResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned message.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQueueResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateQueueResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTopicRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTopicRequest(TeaModel):
    def __init__(
        self,
        enable_logging: bool = None,
        max_message_size: int = None,
        tag: List[CreateTopicRequestTag] = None,
        topic_name: str = None,
    ):
        # Specifies whether to enable the log management feature. Valid values:
        # 
        # *   true: enabled.
        # *   false: disabled. Default value: false.
        self.enable_logging = enable_logging
        # The maximum length of the message that is sent to the topic. Valid values: 1024 to 65536. Unit: bytes. Default value: 65536.
        self.max_message_size = max_message_size
        # The tags.
        self.tag = tag
        # The name of the topic that you want to create.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateTopicRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class CreateTopicResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned message.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateTopicResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateTopicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTopicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventRuleRequest(TeaModel):
    def __init__(
        self,
        product_name: str = None,
        rule_name: str = None,
    ):
        # This parameter is required.
        self.product_name = product_name
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class DeleteEventRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEventRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQueueRequest(TeaModel):
    def __init__(
        self,
        queue_name: str = None,
    ):
        # The name of the queue.
        # 
        # This parameter is required.
        self.queue_name = queue_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        return self


class DeleteQueueResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned message.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQueueResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DeleteQueueResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTopicRequest(TeaModel):
    def __init__(
        self,
        topic_name: str = None,
    ):
        # The name of the topic that you want to delete.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class DeleteTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTopicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint_type: str = None,
    ):
        # The type of the endpoint. Value:
        # 
        # *   **public**: indicates an public endpoint. (Only the public endpoint is supported.)
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        return self


class DisableEndpointResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint_type: str = None,
    ):
        # The type of the endpoint. Valid value:
        # 
        # *   **public**: indicates public endpoint. (Only the public is supported.)
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        return self


class EnableEndpointResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEndpointAttributeRequest(TeaModel):
    def __init__(
        self,
        endpoint_type: str = None,
    ):
        # The type of the endpoint. Value:
        # 
        # *   **public**: indicates public endpoint. (Only the public is supported.)
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        return self


class GetEndpointAttributeResponseBodyDataCidrList(TeaModel):
    def __init__(
        self,
        acl_strategy: str = None,
        cidr: str = None,
        create_time: int = None,
    ):
        # The ACL policy. Valid values:
        # 
        # *   **allow**: indicates that the current endpoint allows access from the corresponding CIDR block. (Only allow is supported.)
        self.acl_strategy = acl_strategy
        # The CIDR block.
        self.cidr = cidr
        # The creation time.
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_strategy is not None:
            result['AclStrategy'] = self.acl_strategy
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStrategy') is not None:
            self.acl_strategy = m.get('AclStrategy')
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class GetEndpointAttributeResponseBodyData(TeaModel):
    def __init__(
        self,
        cidr_list: List[GetEndpointAttributeResponseBodyDataCidrList] = None,
        endpoint_enabled: bool = None,
    ):
        # The list of CIDR block.
        self.cidr_list = cidr_list
        # Specifies whether the endpoint is enabled.
        self.endpoint_enabled = endpoint_enabled

    def validate(self):
        if self.cidr_list:
            for k in self.cidr_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CidrList'] = []
        if self.cidr_list is not None:
            for k in self.cidr_list:
                result['CidrList'].append(k.to_map() if k else None)
        if self.endpoint_enabled is not None:
            result['EndpointEnabled'] = self.endpoint_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cidr_list = []
        if m.get('CidrList') is not None:
            for k in m.get('CidrList'):
                temp_model = GetEndpointAttributeResponseBodyDataCidrList()
                self.cidr_list.append(temp_model.from_map(k))
        if m.get('EndpointEnabled') is not None:
            self.endpoint_enabled = m.get('EndpointEnabled')
        return self


class GetEndpointAttributeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetEndpointAttributeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The response data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetEndpointAttributeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEndpointAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEndpointAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEndpointAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueueAttributesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetQueueAttributesRequest(TeaModel):
    def __init__(
        self,
        queue_name: str = None,
        tag: List[GetQueueAttributesRequestTag] = None,
    ):
        # The name of the queue.
        # 
        # This parameter is required.
        self.queue_name = queue_name
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetQueueAttributesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetQueueAttributesResponseBodyDataDlqPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
        max_receive_count: str = None,
    ):
        # The queue to which dead-letter messages are delivered.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Specifies whether to enable the dead-letter message delivery.
        self.enabled = enabled
        # The maximum number of retries.
        self.max_receive_count = max_receive_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_queue is not None:
            result['DeadLetterTargetQueue'] = self.dead_letter_target_queue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.max_receive_count is not None:
            result['MaxReceiveCount'] = self.max_receive_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('MaxReceiveCount') is not None:
            self.max_receive_count = m.get('MaxReceiveCount')
        return self


class GetQueueAttributesResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetQueueAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        active_messages: int = None,
        create_time: int = None,
        delay_messages: int = None,
        delay_seconds: int = None,
        dlq_policy: GetQueueAttributesResponseBodyDataDlqPolicy = None,
        inactive_messages: int = None,
        last_modify_time: int = None,
        logging_enabled: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        tags: List[GetQueueAttributesResponseBodyDataTags] = None,
        visibility_timeout: int = None,
    ):
        # The total number of messages that are in the Active state in the queue. The value is an approximate value. Default value: 0. We recommend that you do not use the return value and that you call CloudMonitor API operations to query the metric value.
        self.active_messages = active_messages
        # The time when the queue was created.
        self.create_time = create_time
        # The total number of messages that are in the Delayed state in the queue. The value is an approximate value. Default value: 0. We recommend that you do not use the return value and that you call CloudMonitor API operations to query the metric value.
        self.delay_messages = delay_messages
        # The period after which all messages sent to the queue are consumed. Unit: seconds.
        self.delay_seconds = delay_seconds
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # The total number of messages that are in the Inactive state in the queue. The value is an approximate value. Default value: 0. We recommend that you do not use the return value and that you call CloudMonitor API operations to query the metric value.
        self.inactive_messages = inactive_messages
        # The time when the queue was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # Indicates whether the logging feature is enabled. Valid values:
        # 
        # *   True
        # *   False
        self.logging_enabled = logging_enabled
        # The maximum length of the message that is sent to the queue. Unit: bytes.
        self.maximum_message_size = maximum_message_size
        # The maximum duration for which a message is retained in the queue. After the specified retention period ends, the message is deleted regardless of whether the message is received. Unit: seconds.
        self.message_retention_period = message_retention_period
        # The maximum duration for which long polling requests are held after the ReceiveMessage operation is called. Unit: seconds.
        self.polling_wait_seconds = polling_wait_seconds
        # The name of the queue.
        self.queue_name = queue_name
        # The tag.
        self.tags = tags
        # The duration for which a message stays in the Inactive state after the message is received from the queue. Valid values: 1 to 43200. Unit: seconds. Default value: 30.
        self.visibility_timeout = visibility_timeout

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_messages is not None:
            result['ActiveMessages'] = self.active_messages
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_messages is not None:
            result['DelayMessages'] = self.delay_messages
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()
        if self.inactive_messages is not None:
            result['InactiveMessages'] = self.inactive_messages
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveMessages') is not None:
            self.active_messages = m.get('ActiveMessages')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DelayMessages') is not None:
            self.delay_messages = m.get('DelayMessages')
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('DlqPolicy') is not None:
            temp_model = GetQueueAttributesResponseBodyDataDlqPolicy()
            self.dlq_policy = temp_model.from_map(m['DlqPolicy'])
        if m.get('InactiveMessages') is not None:
            self.inactive_messages = m.get('InactiveMessages')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetQueueAttributesResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class GetQueueAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetQueueAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetQueueAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueueAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueueAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQueueAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubscriptionAttributesRequest(TeaModel):
    def __init__(
        self,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        # The name of the subscription.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetSubscriptionAttributesResponseBodyDataDlqPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
    ):
        # The queue to which dead-letter messages are delivered.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Specifies whether to enable the dead-letter message delivery.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_queue is not None:
            result['DeadLetterTargetQueue'] = self.dead_letter_target_queue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class GetSubscriptionAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        dlq_policy: GetSubscriptionAttributesResponseBodyDataDlqPolicy = None,
        endpoint: str = None,
        filter_tag: str = None,
        last_modify_time: int = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
        subscription_name: str = None,
        topic_name: str = None,
        topic_owner: str = None,
    ):
        # The time when the subscription was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # The endpoint to which the messages are pushed.
        self.endpoint = endpoint
        # The tag that is used to filter messages. Only the messages that are attached with the specified tag can be pushed.
        self.filter_tag = filter_tag
        # The time when the subscription was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # The content format of the messages that are pushed to the endpoint. Valid values:
        # 
        # *   XML
        # *   JSON
        # *   SIMPLIFIED
        self.notify_content_format = notify_content_format
        # The retry policy that is applied if an error occurs when Message Service (MNS) pushes messages to the endpoint. Valid values:
        # 
        # *   BACKOFF_RETRY
        # *   EXPONENTIAL_DECAY_RETRY
        self.notify_strategy = notify_strategy
        # The name of the subscription.
        self.subscription_name = subscription_name
        # The name of the topic.
        self.topic_name = topic_name
        # The Alibaba Cloud account ID of the topic owner.
        self.topic_owner = topic_owner

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.filter_tag is not None:
            result['FilterTag'] = self.filter_tag
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.topic_owner is not None:
            result['TopicOwner'] = self.topic_owner
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DlqPolicy') is not None:
            temp_model = GetSubscriptionAttributesResponseBodyDataDlqPolicy()
            self.dlq_policy = temp_model.from_map(m['DlqPolicy'])
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FilterTag') is not None:
            self.filter_tag = m.get('FilterTag')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('TopicOwner') is not None:
            self.topic_owner = m.get('TopicOwner')
        return self


class GetSubscriptionAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetSubscriptionAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSubscriptionAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubscriptionAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubscriptionAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubscriptionAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicAttributesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetTopicAttributesRequest(TeaModel):
    def __init__(
        self,
        tag: List[GetTopicAttributesRequestTag] = None,
        topic_name: str = None,
    ):
        self.tag = tag
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetTopicAttributesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetTopicAttributesResponseBodyDataTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetTopicAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        last_modify_time: int = None,
        logging_enabled: bool = None,
        max_message_size: int = None,
        message_count: int = None,
        message_retention_period: int = None,
        tags: List[GetTopicAttributesResponseBodyDataTags] = None,
        topic_name: str = None,
    ):
        # The time when the topic was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The time when the topic was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # Indicates whether the logging feature is enabled. Valid values:
        # 
        # *   True
        # *   False
        self.logging_enabled = logging_enabled
        # The maximum length of the message that is sent to the topic. Unit: bytes.
        self.max_message_size = max_message_size
        # The number of messages in the topic.
        self.message_count = message_count
        # The maximum duration for which a message is retained in the topic. After the specified retention period ends, the message is deleted regardless of whether the message is received. Unit: seconds.
        self.message_retention_period = message_retention_period
        # The tags added to the resources.
        self.tags = tags
        # The name of the topic.
        self.topic_name = topic_name

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.message_count is not None:
            result['MessageCount'] = self.message_count
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('MessageCount') is not None:
            self.message_count = m.get('MessageCount')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetTopicAttributesResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetTopicAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTopicAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTopicAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTopicAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTopicAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTopicAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListQueueRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        queue_name: str = None,
        tag: List[ListQueueRequestTag] = None,
    ):
        # The page number. Valid values: 1 to 100000000. If you set this parameter to a value smaller than 1, the value of this parameter is 1 by default. If you set this parameter to a value greater than 100000000, the value of this parameter is 100000000 by default.
        self.page_num = page_num
        # The number of entries per page. Value values: 10 to 50. If you set this parameter to a value smaller than 10, the value of this parameter is 10 by default. If you set this parameter to a value greater than 50, the value of this parameter is 50 by default.
        self.page_size = page_size
        # The name of the queue.
        self.queue_name = queue_name
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListQueueRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListQueueResponseBodyDataPageDataDlqPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
        max_receive_count: str = None,
    ):
        # The queue to which dead-letter messages are delivered.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Specifies whether to enable the dead-letter message delivery.
        self.enabled = enabled
        # The maximum number of retries.
        self.max_receive_count = max_receive_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_queue is not None:
            result['DeadLetterTargetQueue'] = self.dead_letter_target_queue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.max_receive_count is not None:
            result['MaxReceiveCount'] = self.max_receive_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('MaxReceiveCount') is not None:
            self.max_receive_count = m.get('MaxReceiveCount')
        return self


class ListQueueResponseBodyDataPageDataTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListQueueResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        active_messages: int = None,
        create_time: int = None,
        delay_messages: int = None,
        delay_seconds: int = None,
        dlq_policy: ListQueueResponseBodyDataPageDataDlqPolicy = None,
        inactive_messages: int = None,
        last_modify_time: int = None,
        logging_enabled: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        tags: List[ListQueueResponseBodyDataPageDataTags] = None,
        visibility_timeout: int = None,
    ):
        # The total number of messages that are in the Active state in the queue. The value is an approximate number. Default value: 0. We recommend that you do not use the return value and that you call CloudMonitor API operations to query the metric value.
        self.active_messages = active_messages
        # The time when the queue was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The total number of the messages that are in the Delayed state in the queue. The value is an approximate number. Default value: 0. We recommend that you do not use the return value and that you call CloudMonitor API operations to query the metric value.
        self.delay_messages = delay_messages
        # The period after which all messages sent to the queue are consumed. Unit: seconds.
        self.delay_seconds = delay_seconds
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # The total number of the messages that are in the Inactive state in the queue. The value is an approximate number. Default value: 0. We recommend that you do not use the return value and that you call CloudMonitor API operations to query the metric value.
        self.inactive_messages = inactive_messages
        # The time when the queue was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # Indicates whether the logging feature is enabled. Valid values:
        # 
        # *   True
        # *   False
        self.logging_enabled = logging_enabled
        # The maximum length of the message that is sent to the queue. Unit: bytes.
        self.maximum_message_size = maximum_message_size
        # The maximum duration for which a message is retained in the queue. After the specified retention period ends, the message is deleted regardless of whether the message is received. Unit: seconds.
        self.message_retention_period = message_retention_period
        # The maximum duration for which long polling requests are held after the ReceiveMessage operation is called. Unit: seconds.
        self.polling_wait_seconds = polling_wait_seconds
        # The name of the queue.
        self.queue_name = queue_name
        # The tags added to the resources.
        self.tags = tags
        # The duration for which a message stays in the Inactive state after the message is received from the queue. Valid values: 1 to 43200. Unit: seconds. Default value: 30.
        self.visibility_timeout = visibility_timeout

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_messages is not None:
            result['ActiveMessages'] = self.active_messages
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_messages is not None:
            result['DelayMessages'] = self.delay_messages
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()
        if self.inactive_messages is not None:
            result['InactiveMessages'] = self.inactive_messages
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveMessages') is not None:
            self.active_messages = m.get('ActiveMessages')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DelayMessages') is not None:
            self.delay_messages = m.get('DelayMessages')
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('DlqPolicy') is not None:
            temp_model = ListQueueResponseBodyDataPageDataDlqPolicy()
            self.dlq_policy = temp_model.from_map(m['DlqPolicy'])
        if m.get('InactiveMessages') is not None:
            self.inactive_messages = m.get('InactiveMessages')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListQueueResponseBodyDataPageDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class ListQueueResponseBodyData(TeaModel):
    def __init__(
        self,
        page_data: List[ListQueueResponseBodyDataPageData] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        size: int = None,
        total: int = None,
    ):
        # The data returned on the current page.
        self.page_data = page_data
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of pages returned.
        self.pages = pages
        # The number of entries on the current page.
        self.size = size
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListQueueResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListQueueResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListQueueResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubscriptionByTopicRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        # The page number. Valid values: 1 to 100000000. If you set this parameter to a value smaller than 1, the value of this parameter is 1 by default. If you set this parameter to a value greater than 100000000, the value of this parameter is 100000000 by default.
        self.page_num = page_num
        # The number of entries per page. Value values: 10 to 50. If you set this parameter to a value smaller than 10, the value of this parameter is 10 by default. If you set this parameter to a value greater than 50, the value of this parameter is 50 by default.
        self.page_size = page_size
        # The name of the subscription.
        self.subscription_name = subscription_name
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class ListSubscriptionByTopicResponseBodyDataPageDataDlqPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
    ):
        # The queue to which dead-letter messages are delivered.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Specifies whether to enable the dead-letter message delivery.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_queue is not None:
            result['DeadLetterTargetQueue'] = self.dead_letter_target_queue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class ListSubscriptionByTopicResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        dlq_policy: ListSubscriptionByTopicResponseBodyDataPageDataDlqPolicy = None,
        endpoint: str = None,
        filter_tag: str = None,
        last_modify_time: int = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
        subscription_name: str = None,
        topic_name: str = None,
        topic_owner: str = None,
    ):
        # The time when the subscription was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # The endpoint to which the messages are pushed.
        self.endpoint = endpoint
        # The tag that is used to filter messages. Only the messages that are attached with the specified tag can be pushed.
        self.filter_tag = filter_tag
        # The time when the subscription was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # The content format of the messages that are pushed to the endpoint. Valid values:
        # 
        # *   XML
        # *   JSON
        # *   SIMPLIFIED
        self.notify_content_format = notify_content_format
        # The retry policy that is applied if an error occurs when Message Service (MNS) pushes messages to the endpoint. Valid values:
        # 
        # *   BACKOFF_RETRY
        # *   EXPONENTIAL_DECAY_RETRY
        self.notify_strategy = notify_strategy
        # The name of the subscription.
        self.subscription_name = subscription_name
        # The name of the topic.
        self.topic_name = topic_name
        # The Alibaba Cloud account ID of the topic owner.
        self.topic_owner = topic_owner

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.filter_tag is not None:
            result['FilterTag'] = self.filter_tag
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.topic_owner is not None:
            result['TopicOwner'] = self.topic_owner
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DlqPolicy') is not None:
            temp_model = ListSubscriptionByTopicResponseBodyDataPageDataDlqPolicy()
            self.dlq_policy = temp_model.from_map(m['DlqPolicy'])
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FilterTag') is not None:
            self.filter_tag = m.get('FilterTag')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('TopicOwner') is not None:
            self.topic_owner = m.get('TopicOwner')
        return self


class ListSubscriptionByTopicResponseBodyData(TeaModel):
    def __init__(
        self,
        page_data: List[ListSubscriptionByTopicResponseBodyDataPageData] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        size: int = None,
        total: int = None,
    ):
        # The data returned on the current page.
        self.page_data = page_data
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of pages returned.
        self.pages = pages
        # The number of entries on the current page.
        self.size = size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.size is not None:
            result['Size'] = self.size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListSubscriptionByTopicResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSubscriptionByTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListSubscriptionByTopicResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListSubscriptionByTopicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSubscriptionByTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubscriptionByTopicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubscriptionByTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTopicRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTopicRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        tag: List[ListTopicRequestTag] = None,
        topic_name: str = None,
    ):
        # The page number. Valid values: 1 to 100000000. If you set this parameter to a value smaller than 1, the value of this parameter is 1 by default. If you set this parameter to a value greater than 100000000, the value of this parameter is 100000000 by default.
        self.page_num = page_num
        # The number of entries per page. Value values: 10 to 50. If you set this parameter to a value smaller than 10, the value of this parameter is 10 by default. If you set this parameter to a value greater than 50, the value of this parameter is 50 by default.
        self.page_size = page_size
        # The tags.
        self.tag = tag
        # The name of the topic.
        self.topic_name = topic_name

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTopicRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class ListTopicResponseBodyDataPageDataTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTopicResponseBodyDataPageData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        last_modify_time: int = None,
        logging_enabled: bool = None,
        max_message_size: int = None,
        message_count: int = None,
        message_retention_period: int = None,
        tags: List[ListTopicResponseBodyDataPageDataTags] = None,
        topic_inner_url: str = None,
        topic_name: str = None,
        topic_url: str = None,
    ):
        # The time when the subscription was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The time when the subscription was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_modify_time = last_modify_time
        # Indicates whether the logging feature is enabled.
        # 
        # *   True
        # *   False
        self.logging_enabled = logging_enabled
        # The maximum length of the message that is sent to the topic. Unit: bytes.
        self.max_message_size = max_message_size
        # The number of messages in the topic.
        self.message_count = message_count
        # The maximum duration for which a message is retained in the topic. After the specified retention period ends, the message is deleted regardless of whether the message is received. Unit: seconds.
        self.message_retention_period = message_retention_period
        # The tags added to the resources.
        self.tags = tags
        # The internal URL of the message topic. The internal URL can be accessed over an internal network.
        self.topic_inner_url = topic_inner_url
        # The name of the topic.
        self.topic_name = topic_name
        # The URL of the message topic.
        self.topic_url = topic_url

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.logging_enabled is not None:
            result['LoggingEnabled'] = self.logging_enabled
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.message_count is not None:
            result['MessageCount'] = self.message_count
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.topic_inner_url is not None:
            result['TopicInnerUrl'] = self.topic_inner_url
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.topic_url is not None:
            result['TopicUrl'] = self.topic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('LoggingEnabled') is not None:
            self.logging_enabled = m.get('LoggingEnabled')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('MessageCount') is not None:
            self.message_count = m.get('MessageCount')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTopicResponseBodyDataPageDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TopicInnerUrl') is not None:
            self.topic_inner_url = m.get('TopicInnerUrl')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('TopicUrl') is not None:
            self.topic_url = m.get('TopicUrl')
        return self


class ListTopicResponseBodyData(TeaModel):
    def __init__(
        self,
        page_data: List[ListTopicResponseBodyDataPageData] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The data returned on the current page.
        self.page_data = page_data
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = ListTopicResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListTopicResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListTopicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTopicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeEndpointAclRequest(TeaModel):
    def __init__(
        self,
        acl_strategy: str = None,
        cidr_list: List[str] = None,
        endpoint_type: str = None,
    ):
        # The ACL policy. Value:
        # 
        # *   **allow**: indicates that this operation is included in the Cidr whitelist. (Only the allow is supported.)
        # 
        # This parameter is required.
        self.acl_strategy = acl_strategy
        # The list of CIDR block.
        # 
        # This parameter is required.
        self.cidr_list = cidr_list
        # The type of the endpoint. Valid values:
        # 
        # *   **public**: indicates public endpoint. (Only the public is supported.)
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_strategy is not None:
            result['AclStrategy'] = self.acl_strategy
        if self.cidr_list is not None:
            result['CidrList'] = self.cidr_list
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStrategy') is not None:
            self.acl_strategy = m.get('AclStrategy')
        if m.get('CidrList') is not None:
            self.cidr_list = m.get('CidrList')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        return self


class RevokeEndpointAclShrinkRequest(TeaModel):
    def __init__(
        self,
        acl_strategy: str = None,
        cidr_list_shrink: str = None,
        endpoint_type: str = None,
    ):
        # The ACL policy. Value:
        # 
        # *   **allow**: indicates that this operation is included in the Cidr whitelist. (Only the allow is supported.)
        # 
        # This parameter is required.
        self.acl_strategy = acl_strategy
        # The list of CIDR block.
        # 
        # This parameter is required.
        self.cidr_list_shrink = cidr_list_shrink
        # The type of the endpoint. Valid values:
        # 
        # *   **public**: indicates public endpoint. (Only the public is supported.)
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_strategy is not None:
            result['AclStrategy'] = self.acl_strategy
        if self.cidr_list_shrink is not None:
            result['CidrList'] = self.cidr_list_shrink
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclStrategy') is not None:
            self.acl_strategy = m.get('AclStrategy')
        if m.get('CidrList') is not None:
            self.cidr_list_shrink = m.get('CidrList')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        return self


class RevokeEndpointAclResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokeEndpointAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeEndpointAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevokeEndpointAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetQueueAttributesRequestDlqPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
        max_receive_count: int = None,
    ):
        # The queue to which dead-letter messages are delivered.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Specifies whether to enable the dead-letter message delivery.
        self.enabled = enabled
        # The maximum number of retries.
        self.max_receive_count = max_receive_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_queue is not None:
            result['DeadLetterTargetQueue'] = self.dead_letter_target_queue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.max_receive_count is not None:
            result['MaxReceiveCount'] = self.max_receive_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('MaxReceiveCount') is not None:
            self.max_receive_count = m.get('MaxReceiveCount')
        return self


class SetQueueAttributesRequest(TeaModel):
    def __init__(
        self,
        delay_seconds: int = None,
        dlq_policy: SetQueueAttributesRequestDlqPolicy = None,
        enable_logging: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        visibility_timeout: int = None,
    ):
        # The period after which all messages sent to the queue are consumed. Valid values: 0 to 604800. Unit: seconds. Default value: 0
        self.delay_seconds = delay_seconds
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # Specifies whether to enable the log management feature. Valid values:
        # 
        # *   true: enabled.
        # *   false: disabled. Default value: false.
        self.enable_logging = enable_logging
        # The maximum length of the message that is sent to the queue. Valid values: 1024 to 65536. Unit: bytes. Default value: 65536.
        self.maximum_message_size = maximum_message_size
        # The maximum duration for which a message is retained in the queue. After the specified retention period ends, the message is deleted regardless of whether the message is received. Valid values: 60 to 604800. Unit: seconds. Default value: 345600.
        self.message_retention_period = message_retention_period
        # The maximum duration for which long polling requests are held after the ReceiveMessage operation is called. Valid values: 0 to 30. Unit: seconds. Default value: 0
        self.polling_wait_seconds = polling_wait_seconds
        # The name of the queue.
        # 
        # This parameter is required.
        self.queue_name = queue_name
        # The duration for which a message stays in the Inactive state after the message is received from the queue. Valid values: 1 to 43200. Unit: seconds. Default value: 30.
        self.visibility_timeout = visibility_timeout

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('DlqPolicy') is not None:
            temp_model = SetQueueAttributesRequestDlqPolicy()
            self.dlq_policy = temp_model.from_map(m['DlqPolicy'])
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class SetQueueAttributesShrinkRequest(TeaModel):
    def __init__(
        self,
        delay_seconds: int = None,
        dlq_policy_shrink: str = None,
        enable_logging: bool = None,
        maximum_message_size: int = None,
        message_retention_period: int = None,
        polling_wait_seconds: int = None,
        queue_name: str = None,
        visibility_timeout: int = None,
    ):
        # The period after which all messages sent to the queue are consumed. Valid values: 0 to 604800. Unit: seconds. Default value: 0
        self.delay_seconds = delay_seconds
        # The dead-letter queue policy.
        self.dlq_policy_shrink = dlq_policy_shrink
        # Specifies whether to enable the log management feature. Valid values:
        # 
        # *   true: enabled.
        # *   false: disabled. Default value: false.
        self.enable_logging = enable_logging
        # The maximum length of the message that is sent to the queue. Valid values: 1024 to 65536. Unit: bytes. Default value: 65536.
        self.maximum_message_size = maximum_message_size
        # The maximum duration for which a message is retained in the queue. After the specified retention period ends, the message is deleted regardless of whether the message is received. Valid values: 60 to 604800. Unit: seconds. Default value: 345600.
        self.message_retention_period = message_retention_period
        # The maximum duration for which long polling requests are held after the ReceiveMessage operation is called. Valid values: 0 to 30. Unit: seconds. Default value: 0
        self.polling_wait_seconds = polling_wait_seconds
        # The name of the queue.
        # 
        # This parameter is required.
        self.queue_name = queue_name
        # The duration for which a message stays in the Inactive state after the message is received from the queue. Valid values: 1 to 43200. Unit: seconds. Default value: 30.
        self.visibility_timeout = visibility_timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.dlq_policy_shrink is not None:
            result['DlqPolicy'] = self.dlq_policy_shrink
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.maximum_message_size is not None:
            result['MaximumMessageSize'] = self.maximum_message_size
        if self.message_retention_period is not None:
            result['MessageRetentionPeriod'] = self.message_retention_period
        if self.polling_wait_seconds is not None:
            result['PollingWaitSeconds'] = self.polling_wait_seconds
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.visibility_timeout is not None:
            result['VisibilityTimeout'] = self.visibility_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('DlqPolicy') is not None:
            self.dlq_policy_shrink = m.get('DlqPolicy')
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaximumMessageSize') is not None:
            self.maximum_message_size = m.get('MaximumMessageSize')
        if m.get('MessageRetentionPeriod') is not None:
            self.message_retention_period = m.get('MessageRetentionPeriod')
        if m.get('PollingWaitSeconds') is not None:
            self.polling_wait_seconds = m.get('PollingWaitSeconds')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VisibilityTimeout') is not None:
            self.visibility_timeout = m.get('VisibilityTimeout')
        return self


class SetQueueAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned message.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetQueueAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SetQueueAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SetQueueAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetQueueAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetQueueAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetQueueAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSubscriptionAttributesRequestDlqPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
    ):
        # The queue to which dead-letter messages are delivered.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Specifies whether to enable the dead-letter message delivery.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_queue is not None:
            result['DeadLetterTargetQueue'] = self.dead_letter_target_queue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class SetSubscriptionAttributesRequest(TeaModel):
    def __init__(
        self,
        dlq_policy: SetSubscriptionAttributesRequestDlqPolicy = None,
        notify_strategy: str = None,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # The retry policy that is applied if an error occurs when Message Service (MNS) pushes messages to the endpoint. Valid values:
        # 
        # *   BACKOFF_RETRY
        # *   EXPONENTIAL_DECAY_RETRY
        self.notify_strategy = notify_strategy
        # The name of the subscription.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DlqPolicy') is not None:
            temp_model = SetSubscriptionAttributesRequestDlqPolicy()
            self.dlq_policy = temp_model.from_map(m['DlqPolicy'])
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SetSubscriptionAttributesShrinkRequest(TeaModel):
    def __init__(
        self,
        dlq_policy_shrink: str = None,
        notify_strategy: str = None,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        # The dead-letter queue policy.
        self.dlq_policy_shrink = dlq_policy_shrink
        # The retry policy that is applied if an error occurs when Message Service (MNS) pushes messages to the endpoint. Valid values:
        # 
        # *   BACKOFF_RETRY
        # *   EXPONENTIAL_DECAY_RETRY
        self.notify_strategy = notify_strategy
        # The name of the subscription.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dlq_policy_shrink is not None:
            result['DlqPolicy'] = self.dlq_policy_shrink
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DlqPolicy') is not None:
            self.dlq_policy_shrink = m.get('DlqPolicy')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SetSubscriptionAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned message.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetSubscriptionAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SetSubscriptionAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SetSubscriptionAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetSubscriptionAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSubscriptionAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetSubscriptionAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetTopicAttributesRequest(TeaModel):
    def __init__(
        self,
        enable_logging: bool = None,
        max_message_size: int = None,
        topic_name: str = None,
    ):
        # Specifies whether to enable the log management feature. Valid values:
        # 
        # *   true: enabled.
        # *   false: disabled. Default value: false.
        self.enable_logging = enable_logging
        # The maximum length of the message that is sent to the topic. Valid values: 1024 to 65536. Unit: bytes. Default value: 65536.
        self.max_message_size = max_message_size
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_logging is not None:
            result['EnableLogging'] = self.enable_logging
        if self.max_message_size is not None:
            result['MaxMessageSize'] = self.max_message_size
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableLogging') is not None:
            self.enable_logging = m.get('EnableLogging')
        if m.get('MaxMessageSize') is not None:
            self.max_message_size = m.get('MaxMessageSize')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SetTopicAttributesResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned message.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetTopicAttributesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: SetTopicAttributesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SetTopicAttributesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetTopicAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetTopicAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SetTopicAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscribeRequestDlqPolicy(TeaModel):
    def __init__(
        self,
        dead_letter_target_queue: str = None,
        enabled: bool = None,
    ):
        # The queue to which dead-letter messages are delivered.
        self.dead_letter_target_queue = dead_letter_target_queue
        # Specifies whether to enable the dead-letter message delivery.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dead_letter_target_queue is not None:
            result['DeadLetterTargetQueue'] = self.dead_letter_target_queue
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeadLetterTargetQueue') is not None:
            self.dead_letter_target_queue = m.get('DeadLetterTargetQueue')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class SubscribeRequest(TeaModel):
    def __init__(
        self,
        dlq_policy: SubscribeRequestDlqPolicy = None,
        endpoint: str = None,
        message_tag: str = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
        push_type: str = None,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        # The dead-letter queue policy.
        self.dlq_policy = dlq_policy
        # The receiver endpoint. The format of the endpoint varies based on the terminal type.
        # 
        # *   If you set PushType to http, set Endpoint to an `HTTP URL that starts with http:// or https://`.
        # *   If you set PushType to queue, set Endpoint to a `queue name`.
        # *   If you set PushType to mpush, set Endpoint to an `AppKey`.
        # *   If you set PushType to alisms, set Endpoint to a `mobile number`.
        # *   If you set PushType to email, set Endpoint to an `email address`.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The tag that is used to filter messages. Only messages that have the same tag can be pushed. Set the value to a string of no more than 16 characters.
        # 
        # By default, no tag is specified to filter messages.
        self.message_tag = message_tag
        # The content format of the messages that are pushed to the endpoint. Valid values:
        # 
        # *   XML
        # *   JSON
        # *   SIMPLIFIED
        self.notify_content_format = notify_content_format
        # The retry policy that is applied if an error occurs when Message Service (MNS) pushes messages to the endpoint. Valid values:
        # 
        # *   BACKOFF_RETRY
        # *   EXPONENTIAL_DECAY_RETRY
        self.notify_strategy = notify_strategy
        # The terminal type. Valid values:
        # 
        # *   http: HTTP services
        # *   queue: queues
        # *   mpush: mobile devices
        # *   alisms: Alibaba Cloud Short Message Service (SMS)
        # *   email: emails
        # 
        # This parameter is required.
        self.push_type = push_type
        # The name of the subscription.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        if self.dlq_policy:
            self.dlq_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dlq_policy is not None:
            result['DlqPolicy'] = self.dlq_policy.to_map()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.message_tag is not None:
            result['MessageTag'] = self.message_tag
        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DlqPolicy') is not None:
            temp_model = SubscribeRequestDlqPolicy()
            self.dlq_policy = temp_model.from_map(m['DlqPolicy'])
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('MessageTag') is not None:
            self.message_tag = m.get('MessageTag')
        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SubscribeShrinkRequest(TeaModel):
    def __init__(
        self,
        dlq_policy_shrink: str = None,
        endpoint: str = None,
        message_tag: str = None,
        notify_content_format: str = None,
        notify_strategy: str = None,
        push_type: str = None,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        # The dead-letter queue policy.
        self.dlq_policy_shrink = dlq_policy_shrink
        # The receiver endpoint. The format of the endpoint varies based on the terminal type.
        # 
        # *   If you set PushType to http, set Endpoint to an `HTTP URL that starts with http:// or https://`.
        # *   If you set PushType to queue, set Endpoint to a `queue name`.
        # *   If you set PushType to mpush, set Endpoint to an `AppKey`.
        # *   If you set PushType to alisms, set Endpoint to a `mobile number`.
        # *   If you set PushType to email, set Endpoint to an `email address`.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The tag that is used to filter messages. Only messages that have the same tag can be pushed. Set the value to a string of no more than 16 characters.
        # 
        # By default, no tag is specified to filter messages.
        self.message_tag = message_tag
        # The content format of the messages that are pushed to the endpoint. Valid values:
        # 
        # *   XML
        # *   JSON
        # *   SIMPLIFIED
        self.notify_content_format = notify_content_format
        # The retry policy that is applied if an error occurs when Message Service (MNS) pushes messages to the endpoint. Valid values:
        # 
        # *   BACKOFF_RETRY
        # *   EXPONENTIAL_DECAY_RETRY
        self.notify_strategy = notify_strategy
        # The terminal type. Valid values:
        # 
        # *   http: HTTP services
        # *   queue: queues
        # *   mpush: mobile devices
        # *   alisms: Alibaba Cloud Short Message Service (SMS)
        # *   email: emails
        # 
        # This parameter is required.
        self.push_type = push_type
        # The name of the subscription.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dlq_policy_shrink is not None:
            result['DlqPolicy'] = self.dlq_policy_shrink
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.message_tag is not None:
            result['MessageTag'] = self.message_tag
        if self.notify_content_format is not None:
            result['NotifyContentFormat'] = self.notify_content_format
        if self.notify_strategy is not None:
            result['NotifyStrategy'] = self.notify_strategy
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DlqPolicy') is not None:
            self.dlq_policy_shrink = m.get('DlqPolicy')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('MessageTag') is not None:
            self.message_tag = m.get('MessageTag')
        if m.get('NotifyContentFormat') is not None:
            self.notify_content_format = m.get('NotifyContentFormat')
        if m.get('NotifyStrategy') is not None:
            self.notify_strategy = m.get('NotifyStrategy')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class SubscribeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubscribeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnsubscribeRequest(TeaModel):
    def __init__(
        self,
        subscription_name: str = None,
        topic_name: str = None,
    ):
        # The name of the subscription.
        # 
        # This parameter is required.
        self.subscription_name = subscription_name
        # The name of the topic.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_name is not None:
            result['SubscriptionName'] = self.subscription_name
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscriptionName') is not None:
            self.subscription_name = m.get('SubscriptionName')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class UnsubscribeResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned message.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnsubscribeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: UnsubscribeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response status.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UnsubscribeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnsubscribeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnsubscribeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnsubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


