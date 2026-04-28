# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarFsObjectsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribePolarFsObjectsResponseBodyItems] = None,
        page_record_count: str = None,
        page_size: str = None,
        path: str = None,
        polar_fs_instance_id: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        self.items = items
        self.page_record_count = page_record_count
        self.page_size = page_size
        self.path = path
        self.polar_fs_instance_id = polar_fs_instance_id
        self.request_id = request_id
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribePolarFsObjectsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribePolarFsObjectsResponseBodyItems(DaraModel):
    def __init__(
        self,
        capacity: str = None,
        creation_time: int = None,
        last_modified: int = None,
        link_target: str = None,
        mode: str = None,
        nlink: int = None,
        owner: str = None,
        path: str = None,
        type: str = None,
    ):
        self.capacity = capacity
        self.creation_time = creation_time
        self.last_modified = last_modified
        self.link_target = link_target
        self.mode = mode
        self.nlink = nlink
        # Owner
        self.owner = owner
        self.path = path
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.link_target is not None:
            result['LinkTarget'] = self.link_target

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.nlink is not None:
            result['Nlink'] = self.nlink

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('LinkTarget') is not None:
            self.link_target = m.get('LinkTarget')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Nlink') is not None:
            self.nlink = m.get('Nlink')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

