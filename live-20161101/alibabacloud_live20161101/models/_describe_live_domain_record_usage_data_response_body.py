# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainRecordUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        record_usage_data: main_models.DescribeLiveDomainRecordUsageDataResponseBodyRecordUsageData = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The recording data that was collected for each interval.
        self.record_usage_data = record_usage_data
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range during which data was queried.
        self.start_time = start_time

    def validate(self):
        if self.record_usage_data:
            self.record_usage_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.record_usage_data is not None:
            result['RecordUsageData'] = self.record_usage_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RecordUsageData') is not None:
            temp_model = main_models.DescribeLiveDomainRecordUsageDataResponseBodyRecordUsageData()
            self.record_usage_data = temp_model.from_map(m.get('RecordUsageData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeLiveDomainRecordUsageDataResponseBodyRecordUsageData(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeLiveDomainRecordUsageDataResponseBodyRecordUsageDataDataModule] = None,
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
                temp_model = main_models.DescribeLiveDomainRecordUsageDataResponseBodyRecordUsageDataDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainRecordUsageDataResponseBodyRecordUsageDataDataModule(DaraModel):
    def __init__(
        self,
        count: int = None,
        domain: str = None,
        duration: int = None,
        region: str = None,
        time_stamp: str = None,
        type: str = None,
    ):
        # The number of peak channels.
        self.count = count
        # The main streaming domain. This parameter is returned if the value of the request parameter SplitBy contains `domain`.
        self.domain = domain
        # The recording length. Unit: seconds.
        self.duration = duration
        # The region ID.
        self.region = region
        # The time when recording started.
        self.time_stamp = time_stamp
        # The recording file type. This parameter is returned if the value of the request parameter SplitBy contains `record_fmt`.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.region is not None:
            result['Region'] = self.region

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

