# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class QueryMemoryListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryMemoryListResponseBodyData = None,
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
            temp_model = main_models.QueryMemoryListResponseBodyData()
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

class QueryMemoryListResponseBodyData(DaraModel):
    def __init__(
        self,
        memory_nodes: List[main_models.QueryMemoryListResponseBodyDataMemoryNodes] = None,
        page_num: str = None,
        page_size: str = None,
        total: str = None,
    ):
        self.memory_nodes = memory_nodes
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

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

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.memory_nodes = []
        if m.get('MemoryNodes') is not None:
            for k1 in m.get('MemoryNodes'):
                temp_model = main_models.QueryMemoryListResponseBodyDataMemoryNodes()
                self.memory_nodes.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryMemoryListResponseBodyDataMemoryNodes(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: int = None,
        event: str = None,
        memory_node_id: str = None,
        meta_data: Dict[str, Any] = None,
        meta_data_json: str = None,
        old_content: str = None,
        project_id: str = None,
        timestamp: int = None,
        update_time: int = None,
    ):
        self.content = content
        self.create_time = create_time
        self.event = event
        self.memory_node_id = memory_node_id
        self.meta_data = meta_data
        self.meta_data_json = meta_data_json
        self.old_content = old_content
        self.project_id = project_id
        self.timestamp = timestamp
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.event is not None:
            result['Event'] = self.event

        if self.memory_node_id is not None:
            result['MemoryNodeId'] = self.memory_node_id

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        if self.meta_data_json is not None:
            result['MetaDataJson'] = self.meta_data_json

        if self.old_content is not None:
            result['OldContent'] = self.old_content

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('MemoryNodeId') is not None:
            self.memory_node_id = m.get('MemoryNodeId')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        if m.get('MetaDataJson') is not None:
            self.meta_data_json = m.get('MetaDataJson')

        if m.get('OldContent') is not None:
            self.old_content = m.get('OldContent')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

