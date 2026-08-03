# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class DescribeUserTrailCountResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeUserTrailCountResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
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
            temp_model = main_models.DescribeUserTrailCountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserTrailCountResponseBodyData(DaraModel):
    def __init__(
        self,
        counts: List[int] = None,
        dates: List[str] = None,
    ):
        # An array of trail counts, where each count corresponds to a date in the `Dates` array.
        self.counts = counts
        # A list of dates.
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

