# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class SenderStatisticsByTagNameAndBatchIDResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        data: main_models.SenderStatisticsByTagNameAndBatchIDResponseBodyData = None,
    ):
        # Request ID
        self.request_id = request_id
        # Total count
        self.total_count = total_count
        # Data records
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('data') is not None:
            temp_model = main_models.SenderStatisticsByTagNameAndBatchIDResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class SenderStatisticsByTagNameAndBatchIDResponseBodyData(DaraModel):
    def __init__(
        self,
        stat: List[main_models.SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat] = None,
    ):
        self.stat = stat

    def validate(self):
        if self.stat:
            for v1 in self.stat:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['stat'] = []
        if self.stat is not None:
            for k1 in self.stat:
                result['stat'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stat = []
        if m.get('stat') is not None:
            for k1 in m.get('stat'):
                temp_model = main_models.SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat()
                self.stat.append(temp_model.from_map(k1))

        return self

class SenderStatisticsByTagNameAndBatchIDResponseBodyDataStat(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        faild_count: str = None,
        request_count: str = None,
        succeeded_percent: str = None,
        success_count: str = None,
        unavailable_count: str = None,
        unavailable_percent: str = None,
    ):
        # Creation time
        self.create_time = create_time
        # Failure count
        self.faild_count = faild_count
        # Request count
        self.request_count = request_count
        # Success rate
        self.succeeded_percent = succeeded_percent
        # Success count
        self.success_count = success_count
        # Invalid count
        self.unavailable_count = unavailable_count
        # Unavailability rate
        self.unavailable_percent = unavailable_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.faild_count is not None:
            result['faildCount'] = self.faild_count

        if self.request_count is not None:
            result['requestCount'] = self.request_count

        if self.succeeded_percent is not None:
            result['succeededPercent'] = self.succeeded_percent

        if self.success_count is not None:
            result['successCount'] = self.success_count

        if self.unavailable_count is not None:
            result['unavailableCount'] = self.unavailable_count

        if self.unavailable_percent is not None:
            result['unavailablePercent'] = self.unavailable_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('faildCount') is not None:
            self.faild_count = m.get('faildCount')

        if m.get('requestCount') is not None:
            self.request_count = m.get('requestCount')

        if m.get('succeededPercent') is not None:
            self.succeeded_percent = m.get('succeededPercent')

        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')

        if m.get('unavailableCount') is not None:
            self.unavailable_count = m.get('unavailableCount')

        if m.get('unavailablePercent') is not None:
            self.unavailable_percent = m.get('unavailablePercent')

        return self

