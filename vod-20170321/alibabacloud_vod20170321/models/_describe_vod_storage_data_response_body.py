# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodStorageDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        request_id: str = None,
        storage_data: main_models.DescribeVodStorageDataResponseBodyStorageData = None,
    ):
        # The time granularity at which the data was queried. Valid values:
        # 
        # *   **hour**
        # *   **day**
        self.data_interval = data_interval
        # The ID of the request.
        self.request_id = request_id
        self.storage_data = storage_data

    def validate(self):
        if self.storage_data:
            self.storage_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.storage_data is not None:
            result['StorageData'] = self.storage_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StorageData') is not None:
            temp_model = main_models.DescribeVodStorageDataResponseBodyStorageData()
            self.storage_data = temp_model.from_map(m.get('StorageData'))

        return self

class DescribeVodStorageDataResponseBodyStorageData(DaraModel):
    def __init__(
        self,
        storage_data_item: List[main_models.DescribeVodStorageDataResponseBodyStorageDataStorageDataItem] = None,
    ):
        self.storage_data_item = storage_data_item

    def validate(self):
        if self.storage_data_item:
            for v1 in self.storage_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StorageDataItem'] = []
        if self.storage_data_item is not None:
            for k1 in self.storage_data_item:
                result['StorageDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.storage_data_item = []
        if m.get('StorageDataItem') is not None:
            for k1 in m.get('StorageDataItem'):
                temp_model = main_models.DescribeVodStorageDataResponseBodyStorageDataStorageDataItem()
                self.storage_data_item.append(temp_model.from_map(k1))

        return self

class DescribeVodStorageDataResponseBodyStorageDataStorageDataItem(DaraModel):
    def __init__(
        self,
        network_out: str = None,
        storage_utilization: str = None,
        time_stamp: str = None,
    ):
        self.network_out = network_out
        self.storage_utilization = storage_utilization
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_out is not None:
            result['NetworkOut'] = self.network_out

        if self.storage_utilization is not None:
            result['StorageUtilization'] = self.storage_utilization

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkOut') is not None:
            self.network_out = m.get('NetworkOut')

        if m.get('StorageUtilization') is not None:
            self.storage_utilization = m.get('StorageUtilization')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

