# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class DescribeUserAlertCountResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeUserAlertCountResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
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
            temp_model = main_models.DescribeUserAlertCountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserAlertCountResponseBodyData(DaraModel):
    def __init__(
        self,
        counts: List[int] = None,
        dates: List[str] = None,
    ):
        # The statistics returned.
        self.counts = counts
        # The dates of alerts.
        self.dates = dates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.counts is not None:
            result['Counts'] = self.counts

        if self.dates is not None:
            result['Dates'] = self.dates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Counts') is not None:
            self.counts = m.get('Counts')

        if m.get('Dates') is not None:
            self.dates = m.get('Dates')

        return self

