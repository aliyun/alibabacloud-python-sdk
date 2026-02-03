# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitorItemsResponseBody(DaraModel):
    def __init__(
        self,
        monitor_items: main_models.DescribeMonitorItemsResponseBodyMonitorItems = None,
        request_id: str = None,
    ):
        # The returned metrics.
        # 
        # > *   **memoryUsage**, **GetQps**, and **PutQps** are supported only by Tair instances that use Redis 4.0 or later. **GetQps** and **PutQps** require the latest minor version. You can upgrade the major version or minor version of the instance as needed. For more information, see [Upgrade the major version](https://help.aliyun.com/document_detail/101764.html) and [Upgrade the minor version](https://help.aliyun.com/document_detail/56450.html).
        # > *   When you use instances of Redis 2.8, if the **hit_rate** metric is not displayed, you must upgrade the minor version of the instance. For more information, see [Upgrade the minor version](https://help.aliyun.com/document_detail/56450.html).
        self.monitor_items = monitor_items
        # The ID of the request.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorItems') is not None:
            temp_model = main_models.DescribeMonitorItemsResponseBodyMonitorItems()
            self.monitor_items = temp_model.from_map(m.get('MonitorItems'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMonitorItemsResponseBodyMonitorItems(DaraModel):
    def __init__(
        self,
        kvstore_monitor_item: List[main_models.DescribeMonitorItemsResponseBodyMonitorItemsKVStoreMonitorItem] = None,
    ):
        self.kvstore_monitor_item = kvstore_monitor_item

    def validate(self):
        if self.kvstore_monitor_item:
            for v1 in self.kvstore_monitor_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KVStoreMonitorItem'] = []
        if self.kvstore_monitor_item is not None:
            for k1 in self.kvstore_monitor_item:
                result['KVStoreMonitorItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kvstore_monitor_item = []
        if m.get('KVStoreMonitorItem') is not None:
            for k1 in m.get('KVStoreMonitorItem'):
                temp_model = main_models.DescribeMonitorItemsResponseBodyMonitorItemsKVStoreMonitorItem()
                self.kvstore_monitor_item.append(temp_model.from_map(k1))

        return self

class DescribeMonitorItemsResponseBodyMonitorItemsKVStoreMonitorItem(DaraModel):
    def __init__(
        self,
        monitor_key: str = None,
        unit: str = None,
    ):
        # The metric.
        self.monitor_key = monitor_key
        # The unit of the metric.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_key is not None:
            result['MonitorKey'] = self.monitor_key

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorKey') is not None:
            self.monitor_key = m.get('MonitorKey')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

