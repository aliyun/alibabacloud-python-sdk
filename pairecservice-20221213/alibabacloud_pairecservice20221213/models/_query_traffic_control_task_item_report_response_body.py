# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class QueryTrafficControlTaskItemReportResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_task_item_reports: List[main_models.QueryTrafficControlTaskItemReportResponseBodyTrafficControlTaskItemReports] = None,
    ):
        self.request_id = request_id
        self.traffic_control_task_item_reports = traffic_control_task_item_reports

    def validate(self):
        if self.traffic_control_task_item_reports:
            for v1 in self.traffic_control_task_item_reports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TrafficControlTaskItemReports'] = []
        if self.traffic_control_task_item_reports is not None:
            for k1 in self.traffic_control_task_item_reports:
                result['TrafficControlTaskItemReports'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.traffic_control_task_item_reports = []
        if m.get('TrafficControlTaskItemReports') is not None:
            for k1 in m.get('TrafficControlTaskItemReports'):
                temp_model = main_models.QueryTrafficControlTaskItemReportResponseBodyTrafficControlTaskItemReports()
                self.traffic_control_task_item_reports.append(temp_model.from_map(k1))

        return self

class QueryTrafficControlTaskItemReportResponseBodyTrafficControlTaskItemReports(DaraModel):
    def __init__(
        self,
        actual_item_control_num: int = None,
        actual_item_control_traffic: int = None,
        done_item_control_num: int = None,
        done_item_control_percentage: str = None,
        item_control_num_percentage: str = None,
        item_control_traffic_percentage: str = None,
        ought_item_control_num: int = None,
        ought_item_control_traffic: int = None,
        traffic_control_target_id: str = None,
        traffic_control_target_name: str = None,
    ):
        self.actual_item_control_num = actual_item_control_num
        self.actual_item_control_traffic = actual_item_control_traffic
        self.done_item_control_num = done_item_control_num
        self.done_item_control_percentage = done_item_control_percentage
        self.item_control_num_percentage = item_control_num_percentage
        self.item_control_traffic_percentage = item_control_traffic_percentage
        self.ought_item_control_num = ought_item_control_num
        self.ought_item_control_traffic = ought_item_control_traffic
        self.traffic_control_target_id = traffic_control_target_id
        self.traffic_control_target_name = traffic_control_target_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_item_control_num is not None:
            result['ActualItemControlNum'] = self.actual_item_control_num

        if self.actual_item_control_traffic is not None:
            result['ActualItemControlTraffic'] = self.actual_item_control_traffic

        if self.done_item_control_num is not None:
            result['DoneItemControlNum'] = self.done_item_control_num

        if self.done_item_control_percentage is not None:
            result['DoneItemControlPercentage'] = self.done_item_control_percentage

        if self.item_control_num_percentage is not None:
            result['ItemControlNumPercentage'] = self.item_control_num_percentage

        if self.item_control_traffic_percentage is not None:
            result['ItemControlTrafficPercentage'] = self.item_control_traffic_percentage

        if self.ought_item_control_num is not None:
            result['OughtItemControlNum'] = self.ought_item_control_num

        if self.ought_item_control_traffic is not None:
            result['OughtItemControlTraffic'] = self.ought_item_control_traffic

        if self.traffic_control_target_id is not None:
            result['TrafficControlTargetId'] = self.traffic_control_target_id

        if self.traffic_control_target_name is not None:
            result['TrafficControlTargetName'] = self.traffic_control_target_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualItemControlNum') is not None:
            self.actual_item_control_num = m.get('ActualItemControlNum')

        if m.get('ActualItemControlTraffic') is not None:
            self.actual_item_control_traffic = m.get('ActualItemControlTraffic')

        if m.get('DoneItemControlNum') is not None:
            self.done_item_control_num = m.get('DoneItemControlNum')

        if m.get('DoneItemControlPercentage') is not None:
            self.done_item_control_percentage = m.get('DoneItemControlPercentage')

        if m.get('ItemControlNumPercentage') is not None:
            self.item_control_num_percentage = m.get('ItemControlNumPercentage')

        if m.get('ItemControlTrafficPercentage') is not None:
            self.item_control_traffic_percentage = m.get('ItemControlTrafficPercentage')

        if m.get('OughtItemControlNum') is not None:
            self.ought_item_control_num = m.get('OughtItemControlNum')

        if m.get('OughtItemControlTraffic') is not None:
            self.ought_item_control_traffic = m.get('OughtItemControlTraffic')

        if m.get('TrafficControlTargetId') is not None:
            self.traffic_control_target_id = m.get('TrafficControlTargetId')

        if m.get('TrafficControlTargetName') is not None:
            self.traffic_control_target_name = m.get('TrafficControlTargetName')

        return self

