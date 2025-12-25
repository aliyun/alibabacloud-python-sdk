# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class ListQueueConsumersResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListQueueConsumersResponseBodyData = None,
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
            temp_model = main_models.ListQueueConsumersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListQueueConsumersResponseBodyData(DaraModel):
    def __init__(
        self,
        consumers: List[main_models.ListQueueConsumersResponseBodyDataConsumers] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The consumers.
        self.consumers = consumers
        # The maximum number of entries returned.
        self.max_results = max_results
        # The token that marks the end of the current returned page. If this parameter is empty, all data is retrieved.
        self.next_token = next_token

    def validate(self):
        if self.consumers:
            for v1 in self.consumers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Consumers'] = []
        if self.consumers is not None:
            for k1 in self.consumers:
                result['Consumers'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumers = []
        if m.get('Consumers') is not None:
            for k1 in m.get('Consumers'):
                temp_model = main_models.ListQueueConsumersResponseBodyDataConsumers()
                self.consumers.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListQueueConsumersResponseBodyDataConsumers(DaraModel):
    def __init__(
        self,
        consumer_tag: str = None,
    ):
        # The consumer tag.
        self.consumer_tag = consumer_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_tag is not None:
            result['ConsumerTag'] = self.consumer_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerTag') is not None:
            self.consumer_tag = m.get('ConsumerTag')

        return self

