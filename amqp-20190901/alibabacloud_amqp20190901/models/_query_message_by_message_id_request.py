# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMessageByMessageIdRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        console_session_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        message_id: str = None,
        page_size: int = None,
        queue_name: str = None,
        vhost_name: str = None,
    ):
        self.begin_time = begin_time
        self.console_session_id = console_session_id
        self.current_page = current_page
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.message_id = message_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

