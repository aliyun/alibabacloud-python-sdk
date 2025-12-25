# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBindingRequest(DaraModel):
    def __init__(
        self,
        binding_key: str = None,
        binding_type: str = None,
        destination_name: str = None,
        instance_id: str = None,
        source_exchange: str = None,
        virtual_host: str = None,
    ):
        # The binding key.
        self.binding_key = binding_key
        # The type of the object that you want to unbind from the source exchange. Valid values:
        # 
        # *   **QUEUE**
        # *   **EXCHANGE**
        # 
        # This parameter is required.
        self.binding_type = binding_type
        # The name of the object that you want to unbind from the source exchange.
        # 
        # This parameter is required.
        self.destination_name = destination_name
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the source exchange.
        # 
        # This parameter is required.
        self.source_exchange = source_exchange
        # The vhost name.
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

