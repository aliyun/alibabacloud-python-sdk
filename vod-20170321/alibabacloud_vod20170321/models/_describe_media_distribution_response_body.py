# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeMediaDistributionResponseBody(DaraModel):
    def __init__(
        self,
        media_distribution_list: List[main_models.DescribeMediaDistributionResponseBodyMediaDistributionList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The distribution list of audio and video media assets. Statistics are displayed based on the statistical period (calendar hour, day, week, or month) within the specified time range.
        self.media_distribution_list = media_distribution_list
        # The request ID.
        self.request_id = request_id
        # The total number of audio and video media assets.
        self.total = total

    def validate(self):
        if self.media_distribution_list:
            for v1 in self.media_distribution_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MediaDistributionList'] = []
        if self.media_distribution_list is not None:
            for k1 in self.media_distribution_list:
                result['MediaDistributionList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media_distribution_list = []
        if m.get('MediaDistributionList') is not None:
            for k1 in m.get('MediaDistributionList'):
                temp_model = main_models.DescribeMediaDistributionResponseBodyMediaDistributionList()
                self.media_distribution_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeMediaDistributionResponseBodyMediaDistributionList(DaraModel):
    def __init__(
        self,
        count: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The number of media assets that match the specified time range within the statistical period.
        self.count = count
        # The end time (exclusive) of the statistical period. Format: yyyy-MM-ddTHH:mm:ssZ (UTC).
        self.end_time = end_time
        # The start time (inclusive) of the statistical period. Format: yyyy-MM-ddTHH:mm:ssZ (UTC).
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

