# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class QueryDedicatedBlockStorageClusterInventoryDataResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryDedicatedBlockStorageClusterInventoryDataResponseBodyData] = None,
        dbsc_id: str = None,
        dbsc_name: str = None,
        disk_category: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the dedicated block storage cluster.
        self.dbsc_id = dbsc_id
        # The name of the dedicated block storage cluster.
        self.dbsc_name = dbsc_name
        # The type of the disk. Valid values:
        # 
        # *   cloud_essd: enhanced SSD (ESSD).
        self.disk_category = disk_category
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.dbsc_id is not None:
            result['DbscId'] = self.dbsc_id

        if self.dbsc_name is not None:
            result['DbscName'] = self.dbsc_name

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryDedicatedBlockStorageClusterInventoryDataResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('DbscId') is not None:
            self.dbsc_id = m.get('DbscId')

        if m.get('DbscName') is not None:
            self.dbsc_name = m.get('DbscName')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryDedicatedBlockStorageClusterInventoryDataResponseBodyData(DaraModel):
    def __init__(
        self,
        monitor_items: main_models.QueryDedicatedBlockStorageClusterInventoryDataResponseBodyDataMonitorItems = None,
        resource_id: str = None,
        timestamp: str = None,
    ):
        # The returned metrics.
        self.monitor_items = monitor_items
        # The ID list of the resource.
        self.resource_id = resource_id
        # The timestamp when the data is collected.
        self.timestamp = timestamp

    def validate(self):
        if self.monitor_items:
            self.monitor_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_items is not None:
            result['MonitorItems'] = self.monitor_items.to_map()

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorItems') is not None:
            temp_model = main_models.QueryDedicatedBlockStorageClusterInventoryDataResponseBodyDataMonitorItems()
            self.monitor_items = temp_model.from_map(m.get('MonitorItems'))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class QueryDedicatedBlockStorageClusterInventoryDataResponseBodyDataMonitorItems(DaraModel):
    def __init__(
        self,
        available_size: int = None,
        total_size: int = None,
    ):
        # Available capacity size of the dedicated block storage cluster.
        self.available_size = available_size
        # Total capacity size of the dedicated block storage cluster.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_size is not None:
            result['AvailableSize'] = self.available_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableSize') is not None:
            self.available_size = m.get('AvailableSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

