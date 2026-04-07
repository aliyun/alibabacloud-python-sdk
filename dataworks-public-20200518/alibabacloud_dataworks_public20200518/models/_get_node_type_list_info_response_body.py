# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetNodeTypeListInfoResponseBody(DaraModel):
    def __init__(
        self,
        node_type_info_list: main_models.GetNodeTypeListInfoResponseBodyNodeTypeInfoList = None,
        request_id: str = None,
    ):
        # The list of node types.
        self.node_type_info_list = node_type_info_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.node_type_info_list:
            self.node_type_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_type_info_list is not None:
            result['NodeTypeInfoList'] = self.node_type_info_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeTypeInfoList') is not None:
            temp_model = main_models.GetNodeTypeListInfoResponseBodyNodeTypeInfoList()
            self.node_type_info_list = temp_model.from_map(m.get('NodeTypeInfoList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNodeTypeListInfoResponseBodyNodeTypeInfoList(DaraModel):
    def __init__(
        self,
        node_type_info: List[main_models.GetNodeTypeListInfoResponseBodyNodeTypeInfoListNodeTypeInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The information about a node type.
        self.node_type_info = node_type_info
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.node_type_info:
            for v1 in self.node_type_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeTypeInfo'] = []
        if self.node_type_info is not None:
            for k1 in self.node_type_info:
                result['NodeTypeInfo'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_type_info = []
        if m.get('NodeTypeInfo') is not None:
            for k1 in m.get('NodeTypeInfo'):
                temp_model = main_models.GetNodeTypeListInfoResponseBodyNodeTypeInfoListNodeTypeInfo()
                self.node_type_info.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetNodeTypeListInfoResponseBodyNodeTypeInfoListNodeTypeInfo(DaraModel):
    def __init__(
        self,
        node_type: int = None,
        node_type_name: str = None,
    ):
        # The type of the node, which is specified by a number.
        self.node_type = node_type
        # The name of the node type.
        self.node_type_name = node_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')

        return self

