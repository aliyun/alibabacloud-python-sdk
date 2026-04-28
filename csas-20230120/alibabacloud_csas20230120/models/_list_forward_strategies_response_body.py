# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListForwardStrategiesResponseBody(DaraModel):
    def __init__(
        self,
        forward_strategies: List[main_models.ListForwardStrategiesResponseBodyForwardStrategies] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        self.forward_strategies = forward_strategies
        # Id of the request
        self.request_id = request_id
        self.total_num = total_num

    def validate(self):
        if self.forward_strategies:
            for v1 in self.forward_strategies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ForwardStrategies'] = []
        if self.forward_strategies is not None:
            for k1 in self.forward_strategies:
                result['ForwardStrategies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forward_strategies = []
        if m.get('ForwardStrategies') is not None:
            for k1 in m.get('ForwardStrategies'):
                temp_model = main_models.ListForwardStrategiesResponseBodyForwardStrategies()
                self.forward_strategies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListForwardStrategiesResponseBodyForwardStrategies(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_id: str = None,
        destination_type: str = None,
        forward_id: str = None,
        name: str = None,
        priority: str = None,
        status: str = None,
    ):
        self.description = description
        self.destination_id = destination_id
        self.destination_type = destination_type
        self.forward_id = forward_id
        self.name = name
        self.priority = priority
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.forward_id is not None:
            result['ForwardId'] = self.forward_id

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('ForwardId') is not None:
            self.forward_id = m.get('ForwardId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

