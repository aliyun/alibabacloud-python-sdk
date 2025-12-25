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
        # *   true: The queue is automatically deleted. After the last consumer unsubscribes from the queue, the queue is automatically deleted.
        # *   false: The queue is not automatically deleted.
        self.auto_delete_state = auto_delete_state
        # The validity period after which the queue is automatically deleted. If the queue is not accessed within the specified period of time, the queue is automatically deleted.
        # 
        # Unit: milliseconds.
        # 
        # >  You can use the feature that corresponds to this parameter only after you enable the feature. To enable the feature, [submit a ticket](https://ticket-intl.console.aliyun.com/#/ticket/createIndex).
        self.auto_expire_state = auto_expire_state
        # The dead-letter exchange. A dead-letter exchange is used to receive rejected messages.
        # 
        # If a consumer rejects a message that cannot be redelivered, ApsaraMQ for RabbitMQ routes the message to the specified dead-letter exchange. Then, the dead-letter exchange routes the message to the queue that is bound to the dead-letter exchange for storage.
        self.dead_letter_exchange = dead_letter_exchange
        # The dead-letter routing key. The key must be 1 to 255 characters in length, and can contain only letters, digits, hyphens (-), underscores (_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        self.dead_letter_routing_key = dead_letter_routing_key
        # Specifies whether the exchange is an exclusive exchange. Valid values:
        # 
        # *   true: The exchange is an exclusive exchange. Only the connection that declares the exclusive exchange can use the exclusive exchange. After the connection is closed, the exclusive exchange is automatically deleted.
        # *   false: The exchange is not an exclusive exchange.
        self.exclusive_state = exclusive_state
        # The ID of the ApsaraMQ for RabbitMQ instance on which you want to create a queue.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is unavailable in the current version of ApsaraMQ for RabbitMQ.
        # 
        # The maximum number of messages that can be stored in the queue. If this threshold is exceeded, the earliest stored messages in the queue are deleted.
        self.max_length = max_length
        # Queue priorities are not supported. The value does not affect the call or return results.
        self.maximum_priority = maximum_priority
        # The message time to live (TTL) of the queue.
        # 
        # *   If the retention period of a message in the queue exceeds the message TTL of the queue, the message expires.
        # *   The message TTL must be set to a non-negative integer. The maximum message TTL is one day. Unit: milliseconds. For example, if the message TTL is 1,000 milliseconds, the message can be retained for up to 1 second in the queue.
        self.message_ttl = message_ttl
        # The name of the queue that you want to create.
        # 
        # *   The name must be 1 to 255 characters in length, and can contain only letters, digits, hyphens (-), underscores (_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        # *   After the queue is created, you cannot change the name of the queue. If you want to change the name of the queue, delete the queue and create another queue.
        # 
        # This parameter is required.
        self.queue_name = queue_name
        # The name of the vhost to which the queue that you want to create belongs. The name must be 1 to 255 characters in length, and can contain only letters, digits, hyphens (-), underscores (_), periods (.), number signs (#), forward slashes (/), and at signs (@).
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

