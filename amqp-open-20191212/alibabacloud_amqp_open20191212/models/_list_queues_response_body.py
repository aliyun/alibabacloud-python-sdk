# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class ListQueuesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListQueuesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListQueuesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListQueuesResponseBodyData(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        queues: List[main_models.ListQueuesResponseBodyDataQueues] = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token
        # The queues.
        self.queues = queues

    def validate(self):
        if self.queues:
            for v1 in self.queues:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Queues'] = []
        if self.queues is not None:
            for k1 in self.queues:
                result['Queues'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.queues = []
        if m.get('Queues') is not None:
            for k1 in m.get('Queues'):
                temp_model = main_models.ListQueuesResponseBodyDataQueues()
                self.queues.append(temp_model.from_map(k1))

        return self

class ListQueuesResponseBodyDataQueues(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        auto_delete_state: bool = None,
        create_time: int = None,
        exclusive_state: bool = None,
        last_consume_time: int = None,
        name: str = None,
        owner_id: str = None,
        vhost_name: str = None,
    ):
        # The attributes.
        self.attributes = attributes
        # Indicates whether the queue was automatically deleted.
        self.auto_delete_state = auto_delete_state
        # The time when the queue was created.
        self.create_time = create_time
        # Indicates whether the queue is an exclusive queue.
        self.exclusive_state = exclusive_state
        # The time when messages in the queue were last consumed.
        self.last_consume_time = last_consume_time
        # The queue name.
        self.name = name
        # The ID of the ApsaraMQ for RabbitMQ instance to which the queue belongs.
        self.owner_id = owner_id
        # The vhost name.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.exclusive_state is not None:
            result['ExclusiveState'] = self.exclusive_state

        if self.last_consume_time is not None:
            result['LastConsumeTime'] = self.last_consume_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.vhost_name is not None:
            result['VHostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExclusiveState') is not None:
            self.exclusive_state = m.get('ExclusiveState')

        if m.get('LastConsumeTime') is not None:
            self.last_consume_time = m.get('LastConsumeTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('VHostName') is not None:
            self.vhost_name = m.get('VHostName')

        return self

