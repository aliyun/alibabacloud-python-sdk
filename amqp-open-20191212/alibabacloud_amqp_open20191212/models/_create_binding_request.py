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
        # The key-value pairs for the message header attributes. The message header attributes consist of one or more key-value pairs. The x-match attribute is required. Other attributes are custom. The x-match attribute supports the following values:
        # 
        # - all: This is the default value. All key-value pairs in the message header must match.
        # 
        # - any: At least one key-value pair in the message header must match.
        # 
        # Separate attributes with semicolons (;) and separate keys from values with colons (:). Example: x-match:all;type:report;format:pdf
        # This parameter is valid only for headers exchanges. For other types of exchanges, this parameter is ignored.
        self.argument = argument
        # The binding key.
        # 
        # - If the source exchange is not a topic exchange:
        # 
        #   - It can contain letters, digits, hyphens (-), underscores (_), periods (.), forward slashes (/), and at signs (@).
        # 
        #   - The length must be 1 to 255 characters.
        # 
        # - If the source exchange is a topic exchange:
        # 
        #   - It can contain letters, digits, hyphens (-), underscores (_), asterisks (\\*), periods (.), number signs (#), forward slashes (/), and at signs (@).
        # 
        #   - The key cannot start or end with a period (.). If the key starts with a number sign (#) or an asterisk (\\*), a period (.) must immediately follow. If the key ends with a number sign (#) or an asterisk (\\*), a period (.) must immediately precede it. If a number sign (#) or an asterisk (\\*) is in the middle of the key, it must have a period (.) on both sides.
        # 
        #   - The length must be 1 to 255 characters.
        self.binding_key = binding_key
        # The type of the destination object. Valid values:
        # 
        # - 0: Queue
        # 
        # - 1: Exchange
        # 
        # This parameter is required.
        self.binding_type = binding_type
        # The name of the binding destination. The destination must be created in the console. It must belong to the same vhost as `SourceExchange`. The `VirtualHost` parameter specifies the vhost.
        # 
        # This parameter is required.
        self.destination_name = destination_name
        # The ID of the ApsaraMQ for RabbitMQ instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the source exchange. This exchange must be created in the console.
        # 
        # This parameter is required.
        self.source_exchange = source_exchange
        # The name of the vhost. The vhost must be created in the console. Both `DestinationName` and `SourceExchange` must belong to this vhost.
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

