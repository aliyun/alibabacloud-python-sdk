# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainTimeShiftDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        time_shift_data: main_models.DescribeLiveDomainTimeShiftDataResponseBodyTimeShiftData = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The time shifting usage data that was collected for each time interval.
        self.time_shift_data = time_shift_data

    def validate(self):
        if self.time_shift_data:
            self.time_shift_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.time_shift_data is not None:
            result['TimeShiftData'] = self.time_shift_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TimeShiftData') is not None:
            temp_model = main_models.DescribeLiveDomainTimeShiftDataResponseBodyTimeShiftData()
            self.time_shift_data = temp_model.from_map(m.get('TimeShiftData'))

        return self

class DescribeLiveDomainTimeShiftDataResponseBodyTimeShiftData(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeLiveDomainTimeShiftDataResponseBodyTimeShiftDataDataModule] = None,
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
                temp_model = main_models.DescribeLiveDomainTimeShiftDataResponseBodyTimeShiftDataDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainTimeShiftDataResponseBodyTimeShiftDataDataModule(DaraModel):
    def __init__(
        self,
        size: str = None,
        time_stamp: str = None,
        type: str = None,
    ):
        # The storage used for time shifting. Unit: bytes.
        self.size = size
        # The timestamp of the data returned.
        self.time_stamp = time_stamp
        # The type of time shifting. Examples: HLS_D1 and HLS_D7.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.size is not None:
            result['Size'] = self.size

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

