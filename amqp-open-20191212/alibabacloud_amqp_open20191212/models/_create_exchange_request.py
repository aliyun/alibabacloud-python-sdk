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
        # The alternate exchange. An alternate exchange is used to receive messages that fail to be routed to queues from the current exchange.
        self.alternate_exchange = alternate_exchange
        # Specifies whether to automatically delete the exchange. Valid values:
        # 
        # *   **true**: If the last queue that is bound to the exchange is unbound, the exchange is automatically deleted.
        # *   **false**: If the last queue that is bound to the exchange is unbound, the exchange is not automatically deleted.
        # 
        # This parameter is required.
        self.auto_delete_state = auto_delete_state
        # The name of the exchange that you want to create. The exchange name must meet the following conventions:
        # 
        # *   The name must be 1 to 255 characters in length, and can contain only letters, digits, hyphens (-), underscores (_), periods (.), number signs (#), forward slashes (/), and at signs (@).
        # *   After the exchange is created, you cannot change its name. If you want to change its name, delete the exchange and create another exchange.
        # 
        # This parameter is required.
        self.exchange_name = exchange_name
        # The exchange type. Valid values:
        # 
        # *   **DIRECT**: An exchange of this type routes a message to the queue whose binding key is exactly the same as the routing key of the message.
        # *   **TOPIC**: This type of exchange is similar to direct exchanges. An exchange of this type routes a message to one or more queues based on the results of the fuzzy match or multi-condition match between the routing key of the message and the binding keys of the current exchange.
        # *   **FANOUT**: An exchange of this type routes all received messages to all queues bound to this exchange. You can use a fanout exchange to broadcast messages.
        # *   **HEADERS**: This type of exchange is similar to direct exchanges. The only difference is that a headers exchange routes messages based on the headers attributes instead of routing keys. When you bind a headers exchange to a queue, you must configure binding attributes in the key-value format for the binding. When you send a message to a headers exchange, you must configure the headers attributes in the key-value format for the message. After a headers exchange receives a message, the exchange routes the message based on the matching results between the headers attributes of the message and the binding attributes of the bound queues.
        # *   **X-CONSISTENT-HASH**: An exchange of this type allows you to perform hash calculations on routing keys or header values and use consistent hashing to route a message to different queues.
        # 
        # This parameter is required.
        self.exchange_type = exchange_type
        # The ID of the ApsaraMQ for RabbitMQ for which you want to create an exchange.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the exchange is an internal exchange. Valid values:
        # 
        # *   **false**
        # *   **true**
        # 
        # This parameter is required.
        self.internal = internal
        # The name of the vhost to which the exchange that you want to create belongs.
        # 
        # This parameter is required.
        self.virtual_host = virtual_host
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

