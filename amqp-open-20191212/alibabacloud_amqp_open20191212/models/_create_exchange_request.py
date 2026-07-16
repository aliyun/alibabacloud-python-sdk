# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExchangeRequest(DaraModel):
    def __init__(
        self,
        alternate_exchange: str = None,
        auto_delete_state: bool = None,
        exchange_name: str = None,
        exchange_type: str = None,
        instance_id: str = None,
        internal: bool = None,
        virtual_host: str = None,
        xdelayed_type: str = None,
    ):
        # The alternate exchange. Configure an alternate exchange to receive messages that fail to be routed.
        self.alternate_exchange = alternate_exchange
        # Specifies whether to automatically delete the exchange. Valid values:
        # 
        # - **true**: Yes. The exchange is automatically deleted after the last queue is unbound from it.
        # 
        # - **false**: No. The exchange is not automatically deleted after the last queue is unbound from it.
        # 
        # This parameter is required.
        self.auto_delete_state = auto_delete_state
        # The name of the exchange. Note:
        # 
        # - The name can contain only letters, digits, hyphens (-), underscores (_), periods (.), number signs (#), forward slashes (/), and at signs (@). The name must be 1 to 255 characters in length.
        # 
        # - The name of an exchange cannot be changed after the exchange is created. To change the name, delete the exchange and create a new one.
        # 
        # This parameter is required.
        self.exchange_name = exchange_name
        # The type of the exchange. Valid values:
        # 
        # - **DIRECT**: This routing rule type routes messages to a queue whose binding key exactly matches the routing key of the message.
        # 
        # - **TOPIC**: This type is similar to the DIRECT type. It routes messages to bound queues using routing key pattern matching and string comparison.
        # 
        # - **FANOUT**: This routing rule type is simple. It routes all messages sent to the exchange to all queues that are bound to the exchange. This works like a broadcast feature.
        # 
        # - **HEADERS**: This type is similar to the DIRECT type. It uses header properties instead of a routing key for routing. When a queue is bound to a headers exchange, key-value pairs are defined for the binding. When a message is sent to the exchange, key-value pairs are defined in the message header. The exchange routes the message by comparing the key-value pairs in the header with the key-value pairs of the binding.
        # 
        # This parameter is required.
        self.exchange_type = exchange_type
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the exchange is an internal exchange. Valid values:
        # 
        # - **false**: No
        # 
        # - **true**: Yes
        # 
        # This parameter is required.
        self.internal = internal
        # The name of the vhost to which the exchange belongs.
        # 
        # This parameter is required.
        self.virtual_host = virtual_host
        # An x-delayed-message exchange lets you use the x-delay header property to specify a delivery delay for a message in milliseconds. The routing rule for the delayed message is determined by the exchange type that you specify for the XDelayedType parameter. This parameter sets the actual exchange type to which the message is delivered after the delay. Valid values:
        # 
        # - **DIRECT**: Delivers the delayed message to the specified queue that is bound to a DIRECT exchange.
        # 
        # - **TOPIC**: Delivers the delayed message to queues that are bound to a TOPIC exchange.
        # 
        # - **FANOUT**: Delivers the delayed message to queues that are bound to a FANOUT exchange.
        # 
        # - **HEADERS**: Delivers the delayed message to queues that are bound to a HEADERS exchange.
        # 
        # - **X-JMS-TOPIC**: Delivers the delayed message to queues that are bound to an X-JMS-TOPIC exchange.
        self.xdelayed_type = xdelayed_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alternate_exchange is not None:
            result['AlternateExchange'] = self.alternate_exchange

        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state

        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name

        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internal is not None:
            result['Internal'] = self.internal

        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host

        if self.xdelayed_type is not None:
            result['XDelayedType'] = self.xdelayed_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlternateExchange') is not None:
            self.alternate_exchange = m.get('AlternateExchange')

        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')

        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')

        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Internal') is not None:
            self.internal = m.get('Internal')

        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')

        if m.get('XDelayedType') is not None:
            self.xdelayed_type = m.get('XDelayedType')

        return self

