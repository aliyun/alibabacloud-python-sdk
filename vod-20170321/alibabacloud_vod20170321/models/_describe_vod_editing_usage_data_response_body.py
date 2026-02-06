# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodEditingUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        editing_data: List[main_models.DescribeVodEditingUsageDataResponseBodyEditingData] = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.editing_data = editing_data
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.editing_data:
            for v1 in self.editing_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EditingData'] = []
        if self.editing_data is not None:
            for k1 in self.editing_data:
                result['EditingData'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.editing_data = []
        if m.get('EditingData') is not None:
            for k1 in m.get('EditingData'):
                temp_model = main_models.DescribeVodEditingUsageDataResponseBodyEditingData()
                self.editing_data.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeVodEditingUsageDataResponseBodyEditingData(DaraModel):
    def __init__(
        self,
        duration: int = None,
        region: str = None,
        specification: str = None,
        time_stamp: str = None,
    ):
        self.duration = duration
        self.region = region
        self.specification = specification
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.region is not None:
            result['Region'] = self.region

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

