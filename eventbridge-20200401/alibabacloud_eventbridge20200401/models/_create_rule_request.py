# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateRuleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        event_targets: List[main_models.CreateRuleRequestEventTargets] = None,
        filter_pattern: str = None,
        rule_name: str = None,
        status: str = None,
    ):
        # The description of the event bus.
        self.description = description
        # The name of the event bus.
        # 
        # This parameter is required.
        self.event_bus_name = event_bus_name
        # The event targets.
        self.event_targets = event_targets
        # The event pattern, in JSON format. Valid values: stringEqual and stringExpression. You can specify up to five expressions in the map data structure in each field.
        # 
        # You can specify up to five expressions in the map data structure in each field.
        # 
        # This parameter is required.
        self.filter_pattern = filter_pattern
        # The name of the event rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The status of the event rule. Valid values: ENABLE: enables the event rule. It is the default status of the event rule. DISABLE: disables the event rule.
        self.status = status

    def validate(self):
        if self.event_targets:
            for v1 in self.event_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        result['EventTargets'] = []
        if self.event_targets is not None:
            for k1 in self.event_targets:
                result['EventTargets'].append(k1.to_map() if k1 else None)

        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        self.event_targets = []
        if m.get('EventTargets') is not None:
            for k1 in m.get('EventTargets'):
                temp_model = main_models.CreateRuleRequestEventTargets()
                self.event_targets.append(temp_model.from_map(k1))

        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class CreateRuleRequestEventTargets(DaraModel):
    def __init__(
        self,
        concurrent_config: main_models.CreateRuleRequestEventTargetsConcurrentConfig = None,
        dead_letter_queue: main_models.CreateRuleRequestEventTargetsDeadLetterQueue = None,
        endpoint: str = None,
        errors_tolerance: str = None,
        id: str = None,
        param_list: List[main_models.CreateRuleRequestEventTargetsParamList] = None,
        push_retry_strategy: str = None,
        type: str = None,
    ):
        # The concurrency configuration.
        self.concurrent_config = concurrent_config
        # The dead-letter queue. Events that are not processed or whose maximum number of retries is exceeded are written to the dead-letter queue. You can use queues in ApsaraMQ for RocketMQ, Simple Message Queue (SMQ, formerly MNS), and ApsaraMQ for Kafka as dead-letter queues. You can also use event buses in EventBridge as dead-letter queues.
        self.dead_letter_queue = dead_letter_queue
        # The endpoint of the event target.
        self.endpoint = endpoint
        # The fault tolerance policy. Valid values: ALL and NONE. The value ALL specifies that fault tolerance is allowed. If an error occurs in an event, event processing is not blocked. If the event fails to be sent after the maximum number of retries specified by the retry policy is reached, the event is delivered to the dead-letter queue or discarded based on your configurations. The value NONE specifies that fault tolerance is not allowed. If an error occurs in an event and the event fails to be sent after the maximum number of retries specified by the retry policy is reached, event processing is blocked.
        self.errors_tolerance = errors_tolerance
        # The ID of the event target.
        # 
        # This parameter is required.
        self.id = id
        # The parameters that are configured for the event target.
        self.param_list = param_list
        # The retry policy that you want to use to push failed events. Valid values: BACKOFF_RETRY and EXPONENTIAL_DECAY_RETRY. BACKOFF_RETRY: A failed event can be retried up to three times. The interval between two consecutive retries is a random value from 10 seconds to 20 seconds. EXPONENTIAL_DECAY_RETRY: A failed event can be retried up to 176 times. The interval between two consecutive retries exponentially increases to a maximum of 512 seconds. The total retry time is 1 day. The specific retry intervals are 1, 2, 4, 8, 16, 32, 64, 128, 256, and 512 seconds. The interval of 512 seconds is used for 167 retries.
        self.push_retry_strategy = push_retry_strategy
        # The type of the event target. For more information, see [Event target parameters](https://help.aliyun.com/document_detail/185887.html).
        # 
        # This parameter is required.
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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrentConfig') is not None:
            temp_model = main_models.CreateRuleRequestEventTargetsConcurrentConfig()
            self.concurrent_config = temp_model.from_map(m.get('ConcurrentConfig'))

        if m.get('DeadLetterQueue') is not None:
            temp_model = main_models.CreateRuleRequestEventTargetsDeadLetterQueue()
            self.dead_letter_queue = temp_model.from_map(m.get('DeadLetterQueue'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ErrorsTolerance') is not None:
            self.errors_tolerance = m.get('ErrorsTolerance')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.CreateRuleRequestEventTargetsParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateRuleRequestEventTargetsParamList(DaraModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format of input parameters for the event target. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        self.form = form
        # The resource key of the event target. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        self.resource_key = resource_key
        # The structure of the template for the event target.
        self.template = template
        # The value of the event target parameter.
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

class CreateRuleRequestEventTargetsDeadLetterQueue(DaraModel):
    def __init__(
        self,
        arn: str = None,
        network: str = None,
        security_group_id: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the dead-letter queue. Events that are not processed or whose maximum number of retries is exceeded are written to the dead-letter queue. Queues in SMQ and ApsaraMQ for RocketMQ can be used as dead-letter queues.
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

class CreateRuleRequestEventTargetsConcurrentConfig(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
    ):
        # The concurrency.
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

