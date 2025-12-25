# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBindingRequest(DaraModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: str = None,
        destination_name: str = None,
        instance_id: str = None,
        source_exchange: str = None,
        virtual_host: str = None,
    ):
        # The key-value pairs that are configured for the headers attributes of a message. One or more key-value pairs can be concatenated to configure the headers attributes of a message. You must specify the x-match attribute as one of the valid values. You can specify custom values for other attributes. Valid values of the x-match attribute:
        # 
        # *   \\*\\*all: \\*\\*A headers exchange routes a message to a queue only if all binding attributes of the queue except for x-match match the headers attributes of the message. This value is the default value.
        # *   \\*\\*any: \\*\\*A headers exchange routes a message to a queue if one or more binding attributes of the queue except for x-match match the headers attributes of the message.
        # 
        # Separate the attributes with semicolons (;). Separate the key and value of an attribute with a colon (:). Example: x-match:all;type:report;format:pdf. This parameter is available for only headers exchanges. You can set this parameter to an arbitrary value for other types of exchanges.
        self.argument = argument
        # The binding key.
        # 
        # *   If the source exchange is not a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain only letters, digits, hyphens (-), underscores (_), periods (.), forward slashes (/), and at signs (@).
        #     *   The binding key must be 1 to 255 characters in length.
        # 
        # *   If the source exchange is a topic exchange, the binding key must meet the following conventions:
        # 
        #     *   The binding key can contain letters, digits, hyphens (-), underscores (_), asterisks (\\*), periods (.), number signs (#), forward slashes (/), and at signs (@).
        #     *   The binding key cannot start or end with a period (.). If a binding key starts with a number sign (#) or an asterisk (\\*), the number sign (#) or asterisk (\\*) must be followed by a period (.). If the binding key ends with a number sign (#) or an asterisk (\\*), the number sign (#) or asterisk (\\*) must be preceded by a period (.). If a number sign (#) or an asterisk (\\*) is used in the middle of a binding key, the number sign (#) or asterisk (\\*) must be preceded and followed by a period (.).
        #     *   The binding key must be 1 to 255 characters in length.
        self.binding_key = binding_key
        # The type of the object that you want to bind to the source exchange. Valid values:
        # 
        # *   \\*\\*0: \\*\\*Queue
        # *   \\*\\*1: \\*\\*Exchange
        # 
        # This parameter is required.
        self.binding_type = binding_type
        # The name of the object that you want to bind to the source exchange. You must create the object in the ApsaraMQ for RabbitMQ console in advance. The vhost of the object is the same as the vhost to which the source exchange specified by **SourceExchange** belongs. The vhost of the source exchange is the one specified by **VirtualHost**.
        # 
        # This parameter is required.
        self.destination_name = destination_name
        # The ID of the ApsaraMQ for RabbitMQ instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the source exchange. You must create the source exchange in the ApsaraMQ for RabbitMQ console in advance.
        # 
        # This parameter is required.
        self.source_exchange = source_exchange
        # The virtual host (vhost) name. You must create the vhost in the ApsaraMQ for RabbitMQ console in advance. The object specified by **DestinationName** and the source exchange specified by **SourceExchange** must belong to the vhost.
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
        if self.argument is not None:
            result['Argument'] = self.argument

        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key

        if self.binding_type is not None:
            result['BindingType'] = self.binding_type

        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange

        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')

        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')

        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')

        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')

        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')

        return self

