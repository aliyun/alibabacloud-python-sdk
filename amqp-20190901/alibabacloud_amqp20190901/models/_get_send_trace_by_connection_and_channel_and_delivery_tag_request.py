# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSendTraceByConnectionAndChannelAndDeliveryTagRequest(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        client_token: str = None,
        connection_id: str = None,
        console_session_id: str = None,
        delivery_tag: int = None,
        end_time: int = None,
        instance_id: str = None,
        start_time: int = None,
        vhost_name: str = None,
    ):
        # This parameter is required.
        self.channel_id = channel_id
        self.client_token = client_token
        # This parameter is required.
        self.connection_id = connection_id
        self.console_session_id = console_session_id
        # This parameter is required.
        self.delivery_tag = delivery_tag
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.delivery_tag is not None:
            result['DeliveryTag'] = self.delivery_tag

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('DeliveryTag') is not None:
            self.delivery_tag = m.get('DeliveryTag')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

