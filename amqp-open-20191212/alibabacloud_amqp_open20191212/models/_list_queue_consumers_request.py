# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQueueConsumersRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        next_token: str = None,
        query_count: int = None,
        queue: str = None,
        virtual_host: str = None,
    ):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token that marks the end of the current page of results. To retrieve the next page, include this token in the next request. If this is your first request or the last page is returned, the value is an empty string.
        self.next_token = next_token
        # The number of entries to return. If you do not set this parameter, the default value is 1.
        # 
        # Valid values: 1 to 100.
        self.query_count = query_count
        # The queue name.
        # 
        # This parameter is required.
        self.queue = queue
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.query_count is not None:
            result['QueryCount'] = self.query_count

        if self.queue is not None:
            result['Queue'] = self.queue

        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')

        if m.get('Queue') is not None:
            self.queue = m.get('Queue')

        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')

        return self

