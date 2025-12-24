# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeUpBpsPeakOfLineResponseBody(DaraModel):
    def __init__(
        self,
        describe_up_bps_peak_of_lines: main_models.DescribeUpBpsPeakOfLineResponseBodyDescribeUpBpsPeakOfLines = None,
        request_id: str = None,
    ):
        # The information about peak inbound bandwidth of the leased line on each day.
        self.describe_up_bps_peak_of_lines = describe_up_bps_peak_of_lines
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.describe_up_bps_peak_of_lines:
            self.describe_up_bps_peak_of_lines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.describe_up_bps_peak_of_lines is not None:
            result['DescribeUpBpsPeakOfLines'] = self.describe_up_bps_peak_of_lines.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DescribeUpBpsPeakOfLines') is not None:
            temp_model = main_models.DescribeUpBpsPeakOfLineResponseBodyDescribeUpBpsPeakOfLines()
            self.describe_up_bps_peak_of_lines = temp_model.from_map(m.get('DescribeUpBpsPeakOfLines'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUpBpsPeakOfLineResponseBodyDescribeUpBpsPeakOfLines(DaraModel):
    def __init__(
        self,
        describe_up_bps_peak_of_line: List[main_models.DescribeUpBpsPeakOfLineResponseBodyDescribeUpBpsPeakOfLinesDescribeUpBpsPeakOfLine] = None,
    ):
        self.describe_up_bps_peak_of_line = describe_up_bps_peak_of_line

    def validate(self):
        if self.describe_up_bps_peak_of_line:
            for v1 in self.describe_up_bps_peak_of_line:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DescribeUpBpsPeakOfLine'] = []
        if self.describe_up_bps_peak_of_line is not None:
            for k1 in self.describe_up_bps_peak_of_line:
                result['DescribeUpBpsPeakOfLine'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.describe_up_bps_peak_of_line = []
        if m.get('DescribeUpBpsPeakOfLine') is not None:
            for k1 in m.get('DescribeUpBpsPeakOfLine'):
                temp_model = main_models.DescribeUpBpsPeakOfLineResponseBodyDescribeUpBpsPeakOfLinesDescribeUpBpsPeakOfLine()
                self.describe_up_bps_peak_of_line.append(temp_model.from_map(k1))

        return self

class DescribeUpBpsPeakOfLineResponseBodyDescribeUpBpsPeakOfLinesDescribeUpBpsPeakOfLine(DaraModel):
    def __init__(
        self,
        band_width: float = None,
        peak_time: str = None,
        query_time: str = None,
        stat_name: str = None,
    ):
        # The daily peak inbound bandwidth of the leased line.
        self.band_width = band_width
        # The time when the daily peak bandwidth of the leased line is reached.
        self.peak_time = peak_time
        # The time queried on the day.
        self.query_time = query_time
        # The category of the statistical data. If the DomainSwitch parameter is set to on, the value of this parameter is the domain name. If the DomainSwitch parameter is set to off or not specified, the value of this parameter is the user ID.
        self.stat_name = stat_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_width is not None:
            result['BandWidth'] = self.band_width

        if self.peak_time is not None:
            result['PeakTime'] = self.peak_time

        if self.query_time is not None:
            result['QueryTime'] = self.query_time

        if self.stat_name is not None:
            result['StatName'] = self.stat_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')

        if m.get('PeakTime') is not None:
            self.peak_time = m.get('PeakTime')

        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')

        if m.get('StatName') is not None:
            self.stat_name = m.get('StatName')

        return self

