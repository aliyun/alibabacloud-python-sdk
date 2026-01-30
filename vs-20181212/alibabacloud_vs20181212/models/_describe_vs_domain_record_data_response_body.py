# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsDomainRecordDataResponseBody(DaraModel):
    def __init__(
        self,
        record_data_per_interval: main_models.DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval = None,
        request_id: str = None,
    ):
        self.record_data_per_interval = record_data_per_interval
        self.request_id = request_id

    def validate(self):
        if self.record_data_per_interval:
            self.record_data_per_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_data_per_interval is not None:
            result['RecordDataPerInterval'] = self.record_data_per_interval.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordDataPerInterval') is not None:
            temp_model = main_models.DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval()
            self.record_data_per_interval = temp_model.from_map(m.get('RecordDataPerInterval'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVsDomainRecordDataResponseBodyRecordDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

    def validate(self):
        if self.data_module:
            for v1 in self.data_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataModule'] = []
        if self.data_module is not None:
            for k1 in self.data_module:
                result['DataModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k1 in m.get('DataModule'):
                temp_model = main_models.DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeVsDomainRecordDataResponseBodyRecordDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        record_value: str = None,
        stream_count_value: str = None,
        time_stamp: str = None,
    ):
        self.record_value = record_value
        self.stream_count_value = stream_count_value
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_value is not None:
            result['RecordValue'] = self.record_value

        if self.stream_count_value is not None:
            result['StreamCountValue'] = self.stream_count_value

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordValue') is not None:
            self.record_value = m.get('RecordValue')

        if m.get('StreamCountValue') is not None:
            self.stream_count_value = m.get('StreamCountValue')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

