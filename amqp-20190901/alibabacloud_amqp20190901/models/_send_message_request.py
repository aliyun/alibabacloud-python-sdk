# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendMessageRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        console_session_id: str = None,
        exchange_name: str = None,
        instance_id: str = None,
        message_id: str = None,
        props: str = None,
        routing_key: str = None,
        vhost_name: str = None,
    ):
        # This parameter is required.
        self.body = body
        self.console_session_id = console_session_id
        # This parameter is required.
        self.exchange_name = exchange_name
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.message_id = message_id
        self.props = props
        # This parameter is required.
        self.routing_key = routing_key
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.props is not None:
            result['Props'] = self.props

        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Props') is not None:
            self.props = m.get('Props')

        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

