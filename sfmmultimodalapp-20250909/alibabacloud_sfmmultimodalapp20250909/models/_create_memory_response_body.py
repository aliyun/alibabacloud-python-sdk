# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class CreateMemoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateMemoryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateMemoryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateMemoryResponseBodyData(DaraModel):
    def __init__(
        self,
        memory_nodes: List[main_models.CreateMemoryResponseBodyDataMemoryNodes] = None,
    ):
        self.memory_nodes = memory_nodes

    def validate(self):
        if self.memory_nodes:
            for v1 in self.memory_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MemoryNodes'] = []
        if self.memory_nodes is not None:
            for k1 in self.memory_nodes:
                result['MemoryNodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.memory_nodes = []
        if m.get('MemoryNodes') is not None:
            for k1 in m.get('MemoryNodes'):
                temp_model = main_models.CreateMemoryResponseBodyDataMemoryNodes()
                self.memory_nodes.append(temp_model.from_map(k1))

        return self

class CreateMemoryResponseBodyDataMemoryNodes(DaraModel):
    def __init__(
        self,
        content: str = None,
        event: str = None,
        memory_node_id: str = None,
        old_content: str = None,
    ):
        self.content = content
        self.event = event
        self.memory_node_id = memory_node_id
        self.old_content = old_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.event is not None:
            result['Event'] = self.event

        if self.memory_node_id is not None:
            result['MemoryNodeId'] = self.memory_node_id

        if self.old_content is not None:
            result['OldContent'] = self.old_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('MemoryNodeId') is not None:
            self.memory_node_id = m.get('MemoryNodeId')

        if m.get('OldContent') is not None:
            self.old_content = m.get('OldContent')

        return self

