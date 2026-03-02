# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQueueRequest(DaraModel):
    def __init__(
        self,
        auto_delete: bool = None,
        auto_expire: int = None,
        console_session_id: str = None,
        dead_letter_exchange: str = None,
        dead_letter_routing_key: str = None,
        exclusive: bool = None,
        instance_id: str = None,
        max_length: int = None,
        maximun_prioty: int = None,
        message_ttl: int = None,
        ordered: bool = None,
        queue_name: str = None,
        retry_inherit: bool = None,
        retry_interval: int = None,
        retry_times: int = None,
        single_active_consumer: bool = None,
        vhost_name: str = None,
    ):
        self.auto_delete = auto_delete
        self.auto_expire = auto_expire
        self.console_session_id = console_session_id
        self.dead_letter_exchange = dead_letter_exchange
        self.dead_letter_routing_key = dead_letter_routing_key
        self.exclusive = exclusive
        self.instance_id = instance_id
        self.max_length = max_length
        self.maximun_prioty = maximun_prioty
        self.message_ttl = message_ttl
        self.ordered = ordered
        # This parameter is required.
        self.queue_name = queue_name
        self.retry_inherit = retry_inherit
        self.retry_interval = retry_interval
        self.retry_times = retry_times
        self.single_active_consumer = single_active_consumer
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_delete is not None:
            result['AutoDelete'] = self.auto_delete

        if self.auto_expire is not None:
            result['AutoExpire'] = self.auto_expire

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.dead_letter_exchange is not None:
            result['DeadLetterExchange'] = self.dead_letter_exchange

        if self.dead_letter_routing_key is not None:
            result['DeadLetterRoutingKey'] = self.dead_letter_routing_key

        if self.exclusive is not None:
            result['Exclusive'] = self.exclusive

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.maximun_prioty is not None:
            result['MaximunPrioty'] = self.maximun_prioty

        if self.message_ttl is not None:
            result['MessageTTL'] = self.message_ttl

        if self.ordered is not None:
            result['Ordered'] = self.ordered

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.retry_inherit is not None:
            result['RetryInherit'] = self.retry_inherit

        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval

        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times

        if self.single_active_consumer is not None:
            result['SingleActiveConsumer'] = self.single_active_consumer

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDelete') is not None:
            self.auto_delete = m.get('AutoDelete')

        if m.get('AutoExpire') is not None:
            self.auto_expire = m.get('AutoExpire')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('DeadLetterExchange') is not None:
            self.dead_letter_exchange = m.get('DeadLetterExchange')

        if m.get('DeadLetterRoutingKey') is not None:
            self.dead_letter_routing_key = m.get('DeadLetterRoutingKey')

        if m.get('Exclusive') is not None:
            self.exclusive = m.get('Exclusive')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('MaximunPrioty') is not None:
            self.maximun_prioty = m.get('MaximunPrioty')

        if m.get('MessageTTL') is not None:
            self.message_ttl = m.get('MessageTTL')

        if m.get('Ordered') is not None:
            self.ordered = m.get('Ordered')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('RetryInherit') is not None:
            self.retry_inherit = m.get('RetryInherit')

        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')

        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')

        if m.get('SingleActiveConsumer') is not None:
            self.single_active_consumer = m.get('SingleActiveConsumer')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

