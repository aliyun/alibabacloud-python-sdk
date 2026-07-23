# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class PutTargetsRequest(DaraModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
        targets: List[main_models.PutTargetsRequestTargets] = None,
    ):
        # The name of the event bus.
        # 
        # This parameter is required.
        self.event_bus_name = event_bus_name
        # The name of the event rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # A list of event targets to create or update. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        # 
        # This parameter is required.
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
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.PutTargetsRequestTargets()
                self.targets.append(temp_model.from_map(k1))

        return self

class PutTargetsRequestTargets(DaraModel):
    def __init__(
        self,
        concurrent_config: main_models.PutTargetsRequestTargetsConcurrentConfig = None,
        dead_letter_queue: main_models.PutTargetsRequestTargetsDeadLetterQueue = None,
        endpoint: str = None,
        errors_tolerance: str = None,
        id: str = None,
        param_list: List[main_models.PutTargetsRequestTargetsParamList] = None,
        push_retry_strategy: str = None,
        type: str = None,
    ):
        # The concurrency control settings.
        self.concurrent_config = concurrent_config
        # The dead-letter queue (DLQ) to which events are sent after all retry attempts fail. Supported DLQ types include Message Queue for Apache RocketMQ, Message Service (MNS), Message Queue for Apache Kafka, and EventBridge.
        self.dead_letter_queue = dead_letter_queue
        # The endpoint of the event target.
        self.endpoint = endpoint
        # The fault tolerance policy. Valid values:
        # 
        # - **ALL**: Enables fault tolerance. If an error occurs, execution continues. After the retry attempts defined by the retry strategy are exhausted, the event is sent to the configured dead-letter queue or discarded.
        # 
        # - **NONE**: Disables fault tolerance. If an error persists after all retry attempts fail, execution is blocked.
        self.errors_tolerance = errors_tolerance
        # The custom ID of the event target.
        # 
        # This parameter is required.
        self.id = id
        # A list of parameters for the event target.
        self.param_list = param_list
        # The retry strategy for pushing events. Valid values:
        # 
        # - **BACKOFF_RETRY**: The event is retried up to three times at random intervals between 10 and 20 seconds.
        # 
        # - **EXPONENTIAL_DECAY_RETRY**: The event is retried up to 176 times over 24 hours. The retry interval starts at 1 second, doubles with each attempt (1, 2, 4, ..., 256 seconds), and is capped at 512 seconds for all subsequent retries.
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
            temp_model = main_models.PutTargetsRequestTargetsConcurrentConfig()
            self.concurrent_config = temp_model.from_map(m.get('ConcurrentConfig'))

        if m.get('DeadLetterQueue') is not None:
            temp_model = main_models.PutTargetsRequestTargetsDeadLetterQueue()
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
                temp_model = main_models.PutTargetsRequestTargetsParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('PushRetryStrategy') is not None:
            self.push_retry_strategy = m.get('PushRetryStrategy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class PutTargetsRequestTargetsParamList(DaraModel):
    def __init__(
        self,
        form: str = None,
        resource_key: str = None,
        template: str = None,
        value: str = None,
    ):
        # The format of the parameter value. For more information, see [Event target parameters](https://help.aliyun.com/document_detail/185887.html).
        self.form = form
        # The key of the parameter. For more information, see [Event target parameters](https://help.aliyun.com/document_detail/185887.html).
        self.resource_key = resource_key
        # The template for the parameter value. This parameter applies only when `Form` is set to `TEMPLATE`.
        self.template = template
        # The value of the parameter.
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

class PutTargetsRequestTargetsDeadLetterQueue(DaraModel):
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
        # The network type of the dead-letter queue.
        self.network = network
        # The security group ID.
        self.security_group_id = security_group_id
        # The VSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
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

class PutTargetsRequestTargetsConcurrentConfig(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
    ):
        # The maximum number of concurrent executions for the event target.
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

