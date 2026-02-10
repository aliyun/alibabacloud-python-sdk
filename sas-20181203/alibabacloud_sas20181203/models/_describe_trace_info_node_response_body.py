# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeTraceInfoNodeResponseBody(DaraModel):
    def __init__(
        self,
        node: main_models.DescribeTraceInfoNodeResponseBodyNode = None,
        request_id: str = None,
    ):
        # The details about the node.
        self.node = node
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node is not None:
            result['Node'] = self.node.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Node') is not None:
            temp_model = main_models.DescribeTraceInfoNodeResponseBodyNode()
            self.node = temp_model.from_map(m.get('Node'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTraceInfoNodeResponseBodyNode(DaraModel):
    def __init__(
        self,
        name: str = None,
        property_list: List[main_models.DescribeTraceInfoNodeResponseBodyNodePropertyList] = None,
        type: str = None,
    ):
        # The name of the node.
        self.name = name
        # An array that consists of the properties of the node.
        self.property_list = property_list
        # The type of the node.
        self.type = type

    def validate(self):
        if self.property_list:
            for v1 in self.property_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        result['PropertyList'] = []
        if self.property_list is not None:
            for k1 in self.property_list:
                result['PropertyList'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.property_list = []
        if m.get('PropertyList') is not None:
            for k1 in m.get('PropertyList'):
                temp_model = main_models.DescribeTraceInfoNodeResponseBodyNodePropertyList()
                self.property_list.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeTraceInfoNodeResponseBodyNodePropertyList(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the property.
        self.name = name
        # The value of the property.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

