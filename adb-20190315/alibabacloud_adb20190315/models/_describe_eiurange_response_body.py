# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeEIURangeResponseBody(DaraModel):
    def __init__(
        self,
        eiuinfo: main_models.DescribeEIURangeResponseBodyEIUInfo = None,
        request_id: str = None,
    ):
        # The queried information about the number of EIUs.
        self.eiuinfo = eiuinfo
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.eiuinfo:
            self.eiuinfo.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eiuinfo is not None:
            result['EIUInfo'] = self.eiuinfo.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EIUInfo') is not None:
            temp_model = main_models.DescribeEIURangeResponseBodyEIUInfo()
            self.eiuinfo = temp_model.from_map(m.get('EIUInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEIURangeResponseBodyEIUInfo(DaraModel):
    def __init__(
        self,
        default_reserved_node_size: str = None,
        default_value: str = None,
        eiurange: List[int] = None,
        max_value: str = None,
        min_value: str = None,
        reserved_node_size_range: List[str] = None,
        step: str = None,
        storage_resource_range: List[str] = None,
    ):
        self.default_reserved_node_size = default_reserved_node_size
        # The suggested value for the number of EIUs.
        self.default_value = default_value
        # The queried range for the number of EIUs.
        self.eiurange = eiurange
        # A reserved parameter.
        self.max_value = max_value
        # A reserved parameter.
        self.min_value = min_value
        self.reserved_node_size_range = reserved_node_size_range
        # A reserved parameter.
        self.step = step
        # A reserved parameter.
        self.storage_resource_range = storage_resource_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_reserved_node_size is not None:
            result['DefaultReservedNodeSize'] = self.default_reserved_node_size

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.eiurange is not None:
            result['EIURange'] = self.eiurange

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.min_value is not None:
            result['MinValue'] = self.min_value

        if self.reserved_node_size_range is not None:
            result['ReservedNodeSizeRange'] = self.reserved_node_size_range

        if self.step is not None:
            result['Step'] = self.step

        if self.storage_resource_range is not None:
            result['StorageResourceRange'] = self.storage_resource_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultReservedNodeSize') is not None:
            self.default_reserved_node_size = m.get('DefaultReservedNodeSize')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('EIURange') is not None:
            self.eiurange = m.get('EIURange')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')

        if m.get('ReservedNodeSizeRange') is not None:
            self.reserved_node_size_range = m.get('ReservedNodeSizeRange')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('StorageResourceRange') is not None:
            self.storage_resource_range = m.get('StorageResourceRange')

        return self

