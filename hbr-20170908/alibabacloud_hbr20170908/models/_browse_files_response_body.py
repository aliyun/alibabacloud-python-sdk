# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class BrowseFilesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        nodes: main_models.BrowseFilesResponseBodyNodes = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.nodes = nodes
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Nodes') is not None:
            temp_model = main_models.BrowseFilesResponseBodyNodes()
            self.nodes = temp_model.from_map(m.get('Nodes'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class BrowseFilesResponseBodyNodes(DaraModel):
    def __init__(
        self,
        node: List[main_models.BrowseFilesResponseBodyNodesNode] = None,
    ):
        self.node = node

    def validate(self):
        if self.node:
            for v1 in self.node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Node'] = []
        if self.node is not None:
            for k1 in self.node:
                result['Node'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node = []
        if m.get('Node') is not None:
            for k1 in m.get('Node'):
                temp_model = main_models.BrowseFilesResponseBodyNodesNode()
                self.node.append(temp_model.from_map(k1))

        return self



class BrowseFilesResponseBodyNodesNode(DaraModel):
    def __init__(
        self,
        name: str = None,
        size: int = None,
        subtree: str = None,
        type: str = None,
    ):
        self.name = name
        self.size = size
        self.subtree = subtree
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.size is not None:
            result['Size'] = self.size

        if self.subtree is not None:
            result['Subtree'] = self.subtree

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Subtree') is not None:
            self.subtree = m.get('Subtree')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

