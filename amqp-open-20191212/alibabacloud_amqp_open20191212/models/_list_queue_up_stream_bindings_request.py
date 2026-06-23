# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQueueUpStreamBindingsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        queue_name: str = None,
        virtual_host: str = None,
    ):
        # The ID of the ApsaraMQ for RabbitMQ instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The maximum number of results to return.
        self.max_results = max_results
        # The token that marks the end of the current query. To retrieve the next page of results, pass this token in the next request. For the first request or when the last page is returned, this parameter is an empty string.
        self.next_token = next_token
        # The queue name.
        # 
        # This parameter is required.
        self.queue_name = queue_name
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')

        return self

