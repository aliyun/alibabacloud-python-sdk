# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQueueRequest(DaraModel):
    def __init__(
        self,
        auto_delete_state: bool = None,
        auto_expire_state: int = None,
        dead_letter_exchange: str = None,
        dead_letter_routing_key: str = None,
        exclusive_state: bool = None,
        instance_id: str = None,
        max_length: int = None,
        maximum_priority: int = None,
        message_ttl: int = None,
        queue_name: str = None,
        virtual_host: str = None,
    ):
        # Specifies whether to automatically delete the queue. Valid values:
        # 
        # - true: The queue is automatically deleted after the last consumer unsubscribes from it.
        # 
        # - false: The queue is not automatically deleted.
        self.auto_delete_state = auto_delete_state
        # The auto-expiration time for the queue. The queue is automatically deleted if it is not accessed within the specified time period.
        # 
        # Unit: milliseconds.
        # 
        # > This feature must be enabled before you can use this parameter. To enable the feature, <props="china">[submit a ticket](https://selfservice.console.aliyun.com/ticket/createIndex)<props="intl">[submit a ticket](https://ticket-intl.console.aliyun.com/#/ticket/createIndex).
        self.auto_expire_state = auto_expire_state
        # The dead-letter exchange. This type of exchange is used to receive rejected messages.
        # 
        # If a consumer rejects a message and the message is not requeued, ApsaraMQ for RabbitMQ routes the message to the specified dead-letter exchange. The dead-letter exchange then routes the message to a bound queue for storage.
        self.dead_letter_exchange = dead_letter_exchange
        # The dead-letter routing key.
        # The key can contain only letters, digits, hyphens (-), underscores (_), periods (.), number signs (#), forward slashes (/), and at signs (@). The key must be 1 to 255 characters in length.
        self.dead_letter_routing_key = dead_letter_routing_key
        # Specifies whether the queue is an exclusive queue. Valid values:
        # 
        # - true: The queue is an exclusive queue. An exclusive queue can be used only by the connection that declares it. The queue is automatically deleted after the connection is closed.
        # 
        # - false: The queue is not an exclusive queue.
        self.exclusive_state = exclusive_state
        # The ID of the ApsaraMQ for RabbitMQ instance to which the queue belongs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is not supported in the current version.
        # 
        # The maximum number of messages that can be stored in the queue. If this limit is exceeded, the earliest messages in the queue are deleted.
        self.max_length = max_length
        # The priority of the queue. The recommended value is an integer from 1 to 10.
        # 
        # > This parameter is used for message priority. It is supported only by dedicated instances and can be used only after the message priority feature is enabled. To enable the feature, <props="china">[submit a ticket](https://selfservice.console.aliyun.com/ticket/createIndex)<props="intl">[submit a ticket](https://ticket-intl.console.aliyun.com/#/ticket/createIndex).
        self.maximum_priority = maximum_priority
        # The time to live (TTL) of a message in the queue.
        # 
        # - A message expires if its retention time in the queue exceeds the configured TTL.
        # 
        # - The message TTL must be a non-negative integer. The maximum value is 1 day. The unit is milliseconds. For example, if the value is 1000, the message can be stored in the queue for a maximum of 1 second.
        self.message_ttl = message_ttl
        # The name of the queue to create.
        # 
        # - The queue name can contain only letters, digits, hyphens (-), underscores (_), periods (.), number signs (#), forward slashes (/), and at signs (@). The name must be 1 to 255 characters in length.
        # 
        # - After a queue is created, its name cannot be changed. To change the name, delete the queue and create a new one.
        # 
        # This parameter is required.
        self.queue_name = queue_name
        # The name of the vhost to which the queue belongs.
        # The name can contain only letters, digits, hyphens (-), underscores (_), periods (.), number signs (#), forward slashes (/), and at signs (@). The name must be 1 to 255 characters in length.
        # 
        # This parameter is required.
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state

        if self.auto_expire_state is not None:
            result['AutoExpireState'] = self.auto_expire_state

        if self.dead_letter_exchange is not None:
            result['DeadLetterExchange'] = self.dead_letter_exchange

        if self.dead_letter_routing_key is not None:
            result['DeadLetterRoutingKey'] = self.dead_letter_routing_key

        if self.exclusive_state is not None:
            result['ExclusiveState'] = self.exclusive_state

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.maximum_priority is not None:
            result['MaximumPriority'] = self.maximum_priority

        if self.message_ttl is not None:
            result['MessageTTL'] = self.message_ttl

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')

        if m.get('AutoExpireState') is not None:
            self.auto_expire_state = m.get('AutoExpireState')

        if m.get('DeadLetterExchange') is not None:
            self.dead_letter_exchange = m.get('DeadLetterExchange')

        if m.get('DeadLetterRoutingKey') is not None:
            self.dead_letter_routing_key = m.get('DeadLetterRoutingKey')

        if m.get('ExclusiveState') is not None:
            self.exclusive_state = m.get('ExclusiveState')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('MaximumPriority') is not None:
            self.maximum_priority = m.get('MaximumPriority')

        if m.get('MessageTTL') is not None:
            self.message_ttl = m.get('MessageTTL')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')

        return self

