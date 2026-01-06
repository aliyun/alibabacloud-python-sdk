# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class GetRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRuleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For a list of error codes, see Error codes.
        self.code = code
        # The returned parameters.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation is successful. If the operation is successful, the value true is returned.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        created_timestamp: int = None,
        description: str = None,
        event_bus_name: str = None,
        filter_pattern: str = None,
        rule_arn: str = None,
        rule_name: str = None,
        status: str = None,
        targets: List[main_models.GetRuleResponseBodyDataTargets] = None,
    ):
        # The timestamp that indicates when the event rule was created.
        self.created_timestamp = created_timestamp
        # The description of the event rule.
        self.description = description
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The event pattern, in JSON format. Valid values: stringEqual and stringExpression. You can specify up to five expressions in the map data structure in each field.
        # 
        # You can specify up to five expressions in the map data structure in each field.
        self.filter_pattern = filter_pattern
        # The Alibaba Cloud Resource Name (ARN) of the event rule.
        self.rule_arn = rule_arn
        # The name of the event rule.
        self.rule_name = rule_name
        # The status of the event rule. Valid values: ENABLE (default): The event rule is enabled. DISABLE: The event rule is disabled.
        self.status = status
        # The event targets.
        self.targets = targets

    def validate(self):
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_timestamp is not None:
            result['CreatedTimestamp'] = self.created_timestamp

        if self.description is not None:
            result['Description'] = self.description

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern

        if self.rule_arn is not None:
            result['RuleARN'] = self.rule_arn

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTimestamp') is not None:
            self.created_timestamp = m.get('CreatedTimestamp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')

        if m.get('RuleARN') is not None:
            self.rule_arn = m.get('RuleARN')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.GetRuleResponseBodyDataTargets()
                self.targets.append(temp_model.from_map(k1))

        return self

class GetRuleResponseBodyDataTargets(DaraModel):
    def __init__(
        self,
        concurrent_config: main_models.GetRuleResponseBodyDataTargetsConcurrentConfig = None,
        dead_letter_queue: main_models.GetRuleResponseBodyDataTargetsDeadLetterQueue = None,
        detail_map: Dict[str, Any] = None,
        endpoint: str = None,
        errors_tolerance: str = None,
        id: str = None,
        param_list: List[main_models.GetRuleResponseBodyDataTargetsParamList] = None,
        push_retry_strategy: str = None,
        push_selector: str = None,
        type: str = None,
    ):
        self.concurrent_config = concurrent_config
        # The dead-letter queue.
        self.dead_letter_queue = dead_letter_queue
        # The information about the event target.
        self.detail_map = detail_map
        # The endpoint of the event target.
        self.endpoint = endpoint
        # The fault tolerance policy. Valid values: ALL and NONE. ALL: Fault tolerance is allowed. If an error occurs in an event, event processing is not blocked. If the event fails to be sent after the maximum number of retries specified by the retry policy is reached, the event is delivered to the dead-letter queue or discarded based on your configurations. NONE: Fault tolerance is not allowed. If an error occurs in an event and the event fails to be sent after the maximum number of retries specified by the retry policy is reached, event processing is blocked.
        self.errors_tolerance = errors_tolerance
        # The ID of the event target.
        self.id = id
        # The parameters that are configured for the event target.
        self.param_list = param_list
        # The retry policy that is used to push failed events. Valid values: BACKOFF_RETRY and EXPONENTIAL_DECAY_RETRY. BACKOFF_RETRY: backoff retry. A failed event can be retried up to three times. The interval between two consecutive retries is a random value between 10 seconds and 20 seconds. EXPONENTIAL_DECAY_RETRY: exponential decay retry. A failed event can be retried up to 176 times. The interval between two consecutive retries exponentially increases to a maximum of 512 seconds. The total retry time is 1 day. The specific retry intervals are 1, 2, 4, 8, 16, 32, 64, 128, 256, and 512 seconds. The interval of 512 seconds is used for 167 retries.
        self.push_retry_strategy = push_retry_strategy
        # The transformer that is used to push events.
        self.push_selector = push_selector
        # The type of the event target. For more information, see [Event target parameters](https://help.aliyun.com/document_detail/185887.html).
        self.type = type

    def validate(self):
        if self.concurrent_config:
            self.concurrent_config.validate()
        if self.dead_letter_queue:
            self.dead_letter_queue.validate()
        if self.param_list:
            for v1 in self.param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrent_config is not None:
            result['ConcurrentConfig'] = self.concurrent_config.to_map()

        if self.dead_letter_queue is not None:
            result['DeadLetterQueue'] = self.dead_letter_queue.to_map()

        if self.detail_map is not None:
            result['DetailMap'] = self.detail_map

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.errors_tolerance is not None:
            result['ErrorsTolerance'] = self.errors_tolerance

        if self.id is not None:
            result['Id'] = self.id

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.push_retry_strategy is not None:
            result['PushRetryStrategy'] = self.push_retry_strategy

        if self.push_selector is not None:
            result['PushSelector'] = self.push_selector

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrentConfig') is not None:
            temp_model = main_models.GetRuleResponseBodyDataTargetsConcurrentConfig()
            self.concurrent_config = temp_model.from_map(m.get('ConcurrentConfig'))

        if m.get('DeadLetterQueue') is not None:
            temp_model = main_models.GetRuleResponseBodyDataTargetsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m.get('DeadLetterQueue'))

        if m.get('DetailMap') is not None:
            self.detail_map = m.get('DetailMap')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.GetRuleResponseBodyDataTargetsParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')

        if m.get('PushSelector') is not None:
            self.push_selector = m.get('PushSelector')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetRuleResponseBodyDataTargetsParamList(DaraModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format that is used by the event target parameter. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        self.form = form
        # The resource key of the event target. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        self.resource_key = resource_key
        # The template based on which events are delivered to the event target.
        self.template = template
        # The event target.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetRuleResponseBodyDataTargetsDeadLetterQueue(DaraModel):
    def __init__(
        self,
        arn: str = None,
        network: str = None,
        security_group_id: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue.
        self.arn = arn
        self.network = network
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.network is not None:
            result['Network'] = self.network

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetRuleResponseBodyDataTargetsConcurrentConfig(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
    ):
        self.concurrency = concurrency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        return self

