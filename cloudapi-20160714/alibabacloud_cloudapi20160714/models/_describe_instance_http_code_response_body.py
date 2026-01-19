# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceHttpCodeResponseBody(DaraModel):
    def __init__(
        self,
        instance_http_code: main_models.DescribeInstanceHttpCodeResponseBodyInstanceHttpCode = None,
        request_id: str = None,
    ):
        # The HTTP status codes.
        self.instance_http_code = instance_http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_http_code:
            self.instance_http_code.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_http_code is not None:
            result['InstanceHttpCode'] = self.instance_http_code.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceHttpCode') is not None:
            temp_model = main_models.DescribeInstanceHttpCodeResponseBodyInstanceHttpCode()
            self.instance_http_code = temp_model.from_map(m.get('InstanceHttpCode'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceHttpCodeResponseBodyInstanceHttpCode(DaraModel):
    def __init__(
        self,
        monitor_item: List[main_models.DescribeInstanceHttpCodeResponseBodyInstanceHttpCodeMonitorItem] = None,
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
                temp_model = main_models.DescribeInstanceHttpCodeResponseBodyInstanceHttpCodeMonitorItem()
                self.monitor_item.append(temp_model.from_map(k1))

        return self

class DescribeInstanceHttpCodeResponseBodyInstanceHttpCodeMonitorItem(DaraModel):
    def __init__(
        self,
        item_time: str = None,
        item_value: str = None,
    ):
        # The HTTP status code returned.
        self.item_time = item_time
        # The corresponding value.
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

