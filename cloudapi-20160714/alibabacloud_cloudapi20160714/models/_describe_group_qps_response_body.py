# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupQpsResponseBody(DaraModel):
    def __init__(
        self,
        group_qps: main_models.DescribeGroupQpsResponseBodyGroupQps = None,
        request_id: str = None,
    ):
        # The number of requests directed to the API group.
        self.group_qps = group_qps
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.group_qps:
            self.group_qps.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_qps is not None:
            result['GroupQps'] = self.group_qps.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupQps') is not None:
            temp_model = main_models.DescribeGroupQpsResponseBodyGroupQps()
            self.group_qps = temp_model.from_map(m.get('GroupQps'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGroupQpsResponseBodyGroupQps(DaraModel):
    def __init__(
        self,
        monitor_item: List[main_models.DescribeGroupQpsResponseBodyGroupQpsMonitorItem] = None,
    ):
        self.monitor_item = monitor_item

    def validate(self):
        if self.monitor_item:
            for v1 in self.monitor_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MonitorItem'] = []
        if self.monitor_item is not None:
            for k1 in self.monitor_item:
                result['MonitorItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_item = []
        if m.get('MonitorItem') is not None:
            for k1 in m.get('MonitorItem'):
                temp_model = main_models.DescribeGroupQpsResponseBodyGroupQpsMonitorItem()
                self.monitor_item.append(temp_model.from_map(k1))

        return self

class DescribeGroupQpsResponseBodyGroupQpsMonitorItem(DaraModel):
    def __init__(
        self,
        item_time: str = None,
        item_value: str = None,
    ):
        # The point in time.
        self.item_time = item_time
        # The number of requests at the specified point in time.
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_time is not None:
            result['ItemTime'] = self.item_time

        if self.item_value is not None:
            result['ItemValue'] = self.item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTime') is not None:
            self.item_time = m.get('ItemTime')

        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')

        return self

