# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowStatisticResponseBody(DaraModel):
    def __init__(
        self,
        desktop_count: int = None,
        desktop_flow_statistic: List[main_models.DescribeFlowStatisticResponseBodyDesktopFlowStatistic] = None,
        request_id: str = None,
    ):
        # The number of available cloud computers in the office network.
        self.desktop_count = desktop_count
        # The traffic statistics.
        self.desktop_flow_statistic = desktop_flow_statistic
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.desktop_flow_statistic:
            for v1 in self.desktop_flow_statistic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count

        result['DesktopFlowStatistic'] = []
        if self.desktop_flow_statistic is not None:
            for k1 in self.desktop_flow_statistic:
                result['DesktopFlowStatistic'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')

        self.desktop_flow_statistic = []
        if m.get('DesktopFlowStatistic') is not None:
            for k1 in m.get('DesktopFlowStatistic'):
                temp_model = main_models.DescribeFlowStatisticResponseBodyDesktopFlowStatistic()
                self.desktop_flow_statistic.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFlowStatisticResponseBodyDesktopFlowStatistic(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
        flow_in: str = None,
        flow_rank: int = None,
    ):
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The name of the cloud computer.
        self.desktop_name = desktop_name
        # The traffic amount. Unit: KB.
        self.flow_in = flow_in
        # The traffic ranking.
        self.flow_rank = flow_rank

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.flow_in is not None:
            result['FlowIn'] = self.flow_in

        if self.flow_rank is not None:
            result['FlowRank'] = self.flow_rank

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('FlowIn') is not None:
            self.flow_in = m.get('FlowIn')

        if m.get('FlowRank') is not None:
            self.flow_rank = m.get('FlowRank')

        return self

