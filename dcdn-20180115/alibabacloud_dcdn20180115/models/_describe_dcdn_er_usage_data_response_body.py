# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnErUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        er_acc_data: main_models.DescribeDcdnErUsageDataResponseBodyErAccData = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The list of the data returned.
        self.er_acc_data = er_acc_data
        # The ID of the request.
        self.request_id = request_id
        # The start of the time range during which data was queried.
        self.start_time = start_time

    def validate(self):
        if self.er_acc_data:
            self.er_acc_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.er_acc_data is not None:
            result['ErAccData'] = self.er_acc_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ErAccData') is not None:
            temp_model = main_models.DescribeDcdnErUsageDataResponseBodyErAccData()
            self.er_acc_data = temp_model.from_map(m.get('ErAccData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDcdnErUsageDataResponseBodyErAccData(DaraModel):
    def __init__(
        self,
        er_acc_item: List[main_models.DescribeDcdnErUsageDataResponseBodyErAccDataErAccItem] = None,
    ):
        self.er_acc_item = er_acc_item

    def validate(self):
        if self.er_acc_item:
            for v1 in self.er_acc_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErAccItem'] = []
        if self.er_acc_item is not None:
            for k1 in self.er_acc_item:
                result['ErAccItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.er_acc_item = []
        if m.get('ErAccItem') is not None:
            for k1 in m.get('ErAccItem'):
                temp_model = main_models.DescribeDcdnErUsageDataResponseBodyErAccDataErAccItem()
                self.er_acc_item.append(temp_model.from_map(k1))

        return self

class DescribeDcdnErUsageDataResponseBodyErAccDataErAccItem(DaraModel):
    def __init__(
        self,
        er_acc: int = None,
        routine: str = None,
        spec: str = None,
        time_stamp: str = None,
    ):
        # The number of requests.
        self.er_acc = er_acc
        # The ID of the routine. This parameter is returned only when SplitBy is set to routine.
        self.routine = routine
        # The specification of the routine. This parameter is returned only when SplitBy is set to spec.
        self.spec = spec
        # The timestamp of the returned data.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.er_acc is not None:
            result['ErAcc'] = self.er_acc

        if self.routine is not None:
            result['Routine'] = self.routine

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErAcc') is not None:
            self.er_acc = m.get('ErAcc')

        if m.get('Routine') is not None:
            self.routine = m.get('Routine')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

