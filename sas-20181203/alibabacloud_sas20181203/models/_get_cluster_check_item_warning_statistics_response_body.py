# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetClusterCheckItemWarningStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetClusterCheckItemWarningStatisticsResponseBodyData = None,
        request_id: str = None,
    ):
        # The statistics on risk items by risk level.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetClusterCheckItemWarningStatisticsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetClusterCheckItemWarningStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        high_warning_count: int = None,
        low_warning_count: int = None,
        medium_warning_count: int = None,
    ):
        # The number of high-risk items.
        self.high_warning_count = high_warning_count
        # The number of low-risk items.
        self.low_warning_count = low_warning_count
        # The number of medium-risk items.
        self.medium_warning_count = medium_warning_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.high_warning_count is not None:
            result['HighWarningCount'] = self.high_warning_count

        if self.low_warning_count is not None:
            result['LowWarningCount'] = self.low_warning_count

        if self.medium_warning_count is not None:
            result['MediumWarningCount'] = self.medium_warning_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HighWarningCount') is not None:
            self.high_warning_count = m.get('HighWarningCount')

        if m.get('LowWarningCount') is not None:
            self.low_warning_count = m.get('LowWarningCount')

        if m.get('MediumWarningCount') is not None:
            self.medium_warning_count = m.get('MediumWarningCount')

        return self

