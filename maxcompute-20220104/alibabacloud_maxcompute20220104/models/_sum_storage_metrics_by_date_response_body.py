# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class SumStorageMetricsByDateResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.SumStorageMetricsByDateResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.SumStorageMetricsByDateResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SumStorageMetricsByDateResponseBodyData(DaraModel):
    def __init__(
        self,
        date_time: str = None,
        item_storage_metrics: List[main_models.SumStorageMetricsByDateResponseBodyDataItemStorageMetrics] = None,
        storage_type: str = None,
        unit: str = None,
        usage: str = None,
    ):
        self.date_time = date_time
        self.item_storage_metrics = item_storage_metrics
        self.storage_type = storage_type
        self.unit = unit
        self.usage = usage

    def validate(self):
        if self.item_storage_metrics:
            for v1 in self.item_storage_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_time is not None:
            result['dateTime'] = self.date_time

        result['itemStorageMetrics'] = []
        if self.item_storage_metrics is not None:
            for k1 in self.item_storage_metrics:
                result['itemStorageMetrics'].append(k1.to_map() if k1 else None)

        if self.storage_type is not None:
            result['storageType'] = self.storage_type

        if self.unit is not None:
            result['unit'] = self.unit

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')

        self.item_storage_metrics = []
        if m.get('itemStorageMetrics') is not None:
            for k1 in m.get('itemStorageMetrics'):
                temp_model = main_models.SumStorageMetricsByDateResponseBodyDataItemStorageMetrics()
                self.item_storage_metrics.append(temp_model.from_map(k1))

        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

class SumStorageMetricsByDateResponseBodyDataItemStorageMetrics(DaraModel):
    def __init__(
        self,
        item_name: str = None,
        percentage: float = None,
        usage: str = None,
    ):
        self.item_name = item_name
        self.percentage = percentage
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_name is not None:
            result['itemName'] = self.item_name

        if self.percentage is not None:
            result['percentage'] = self.percentage

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')

        if m.get('percentage') is not None:
            self.percentage = m.get('percentage')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

