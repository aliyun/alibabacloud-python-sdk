# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeEndPointEventListResponseBody(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeEndPointEventListResponseBodyNodes] = None,
        request_id: str = None,
    ):
        self.nodes = nodes
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeEndPointEventListResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEndPointEventListResponseBodyNodes(DaraModel):
    def __init__(
        self,
        event_data_items: List[main_models.DescribeEndPointEventListResponseBodyNodesEventDataItems] = None,
        user_id: str = None,
    ):
        self.event_data_items = event_data_items
        self.user_id = user_id

    def validate(self):
        if self.event_data_items:
            for v1 in self.event_data_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventDataItems'] = []
        if self.event_data_items is not None:
            for k1 in self.event_data_items:
                result['EventDataItems'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_data_items = []
        if m.get('EventDataItems') is not None:
            for k1 in m.get('EventDataItems'):
                temp_model = main_models.DescribeEndPointEventListResponseBodyNodesEventDataItems()
                self.event_data_items.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeEndPointEventListResponseBodyNodesEventDataItems(DaraModel):
    def __init__(
        self,
        event_list: List[main_models.DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList] = None,
        ts: int = None,
    ):
        self.event_list = event_list
        self.ts = ts

    def validate(self):
        if self.event_list:
            for v1 in self.event_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventList'] = []
        if self.event_list is not None:
            for k1 in self.event_list:
                result['EventList'].append(k1.to_map() if k1 else None)

        if self.ts is not None:
            result['Ts'] = self.ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k1 in m.get('EventList'):
                temp_model = main_models.DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList()
                self.event_list.append(temp_model.from_map(k1))

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        return self

class DescribeEndPointEventListResponseBodyNodesEventDataItemsEventList(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        event_type: str = None,
        ts: int = None,
        ts_in_ms: str = None,
    ):
        self.event_name = event_name
        self.event_type = event_type
        self.ts = ts
        self.ts_in_ms = ts_in_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.ts is not None:
            result['Ts'] = self.ts

        if self.ts_in_ms is not None:
            result['TsInMs'] = self.ts_in_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        if m.get('TsInMs') is not None:
            self.ts_in_ms = m.get('TsInMs')

        return self

