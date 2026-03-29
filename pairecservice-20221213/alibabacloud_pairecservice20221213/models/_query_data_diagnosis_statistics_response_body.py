# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class QueryDataDiagnosisStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        statistics: main_models.QueryDataDiagnosisStatisticsResponseBodyStatistics = None,
    ):
        self.request_id = request_id
        self.statistics = statistics

    def validate(self):
        if self.statistics:
            self.statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.statistics is not None:
            result['Statistics'] = self.statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Statistics') is not None:
            temp_model = main_models.QueryDataDiagnosisStatisticsResponseBodyStatistics()
            self.statistics = temp_model.from_map(m.get('Statistics'))

        return self

class QueryDataDiagnosisStatisticsResponseBodyStatistics(DaraModel):
    def __init__(
        self,
        failed_dates: List[str] = None,
        no_data_dates: List[str] = None,
    ):
        self.failed_dates = failed_dates
        self.no_data_dates = no_data_dates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_dates is not None:
            result['FailedDates'] = self.failed_dates

        if self.no_data_dates is not None:
            result['NoDataDates'] = self.no_data_dates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedDates') is not None:
            self.failed_dates = m.get('FailedDates')

        if m.get('NoDataDates') is not None:
            self.no_data_dates = m.get('NoDataDates')

        return self

