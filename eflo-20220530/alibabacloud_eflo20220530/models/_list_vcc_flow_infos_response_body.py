# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListVccFlowInfosResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.ListVccFlowInfosResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # 访问被拒绝的详细原因。
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The returned data.
        self.content = content
        # Response
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Content') is not None:
            temp_model = main_models.ListVccFlowInfosResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListVccFlowInfosResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListVccFlowInfosResponseBodyContentData] = None,
        total: int = None,
    ):
        # Lingjun Connection Traffic Information
        self.data = data
        # The total number of entries returned.
        self.total = total

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

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListVccFlowInfosResponseBodyContentData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListVccFlowInfosResponseBodyContentData(DaraModel):
    def __init__(
        self,
        direction: str = None,
        metric_name: str = None,
        region_id: str = None,
        timestamp: int = None,
        value: float = None,
        vcc_id: str = None,
    ):
        # The direction.
        self.direction = direction
        # The metric. Valid values:
        self.metric_name = metric_name
        # The region ID.
        self.region_id = region_id
        # Time
        self.timestamp = timestamp
        # Value
        self.value = value
        # Lingjun Connection ID
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.value is not None:
            result['Value'] = self.value

        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')

        return self

