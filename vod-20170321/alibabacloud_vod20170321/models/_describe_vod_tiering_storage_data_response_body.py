# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodTieringStorageDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        storage_data: List[main_models.DescribeVodTieringStorageDataResponseBodyStorageData] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The storage usage data.
        self.storage_data = storage_data

    def validate(self):
        if self.storage_data:
            for v1 in self.storage_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StorageData'] = []
        if self.storage_data is not None:
            for k1 in self.storage_data:
                result['StorageData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.storage_data = []
        if m.get('StorageData') is not None:
            for k1 in m.get('StorageData'):
                temp_model = main_models.DescribeVodTieringStorageDataResponseBodyStorageData()
                self.storage_data.append(temp_model.from_map(k1))

        return self

class DescribeVodTieringStorageDataResponseBodyStorageData(DaraModel):
    def __init__(
        self,
        lessthan_month_datasize: int = None,
        region: str = None,
        storage_class: str = None,
        storage_utilization: int = None,
        time_stamp: str = None,
    ):
        # The size of data stored for less than one month. Unit: bytes.
        self.lessthan_month_datasize = lessthan_month_datasize
        # The storage region.
        self.region = region
        # The storage class.
        self.storage_class = storage_class
        # The storage usage. Unit: bytes.
        self.storage_utilization = storage_utilization
        # The start time of the time interval. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lessthan_month_datasize is not None:
            result['LessthanMonthDatasize'] = self.lessthan_month_datasize

        if self.region is not None:
            result['Region'] = self.region

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.storage_utilization is not None:
            result['StorageUtilization'] = self.storage_utilization

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LessthanMonthDatasize') is not None:
            self.lessthan_month_datasize = m.get('LessthanMonthDatasize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('StorageUtilization') is not None:
            self.storage_utilization = m.get('StorageUtilization')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

