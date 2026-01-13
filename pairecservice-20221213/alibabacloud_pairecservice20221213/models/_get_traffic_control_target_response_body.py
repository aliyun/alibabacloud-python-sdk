# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class GetTrafficControlTargetResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        gmt_create_time: str = None,
        item_condition_array: str = None,
        item_condition_express: str = None,
        item_condition_type: str = None,
        name: str = None,
        new_product_regulation: bool = None,
        recall_name: str = None,
        request_id: str = None,
        split_parts: main_models.GetTrafficControlTargetResponseBodySplitParts = None,
        start_time: str = None,
        statis_period: str = None,
        status: str = None,
        tolerance_value: int = None,
        traffic_control_target_id: str = None,
        traffic_control_task_id: str = None,
        value: float = None,
    ):
        self.end_time = end_time
        self.event = event
        self.gmt_create_time = gmt_create_time
        self.item_condition_array = item_condition_array
        self.item_condition_express = item_condition_express
        self.item_condition_type = item_condition_type
        self.name = name
        self.new_product_regulation = new_product_regulation
        self.recall_name = recall_name
        self.request_id = request_id
        self.split_parts = split_parts
        self.start_time = start_time
        self.statis_period = statis_period
        self.status = status
        self.tolerance_value = tolerance_value
        self.traffic_control_target_id = traffic_control_target_id
        self.traffic_control_task_id = traffic_control_task_id
        self.value = value

    def validate(self):
        if self.split_parts:
            self.split_parts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event is not None:
            result['Event'] = self.event

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array

        if self.item_condition_express is not None:
            result['ItemConditionExpress'] = self.item_condition_express

        if self.item_condition_type is not None:
            result['ItemConditionType'] = self.item_condition_type

        if self.name is not None:
            result['Name'] = self.name

        if self.new_product_regulation is not None:
            result['NewProductRegulation'] = self.new_product_regulation

        if self.recall_name is not None:
            result['RecallName'] = self.recall_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.split_parts is not None:
            result['SplitParts'] = self.split_parts.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statis_period is not None:
            result['StatisPeriod'] = self.statis_period

        if self.status is not None:
            result['Status'] = self.status

        if self.tolerance_value is not None:
            result['ToleranceValue'] = self.tolerance_value

        if self.traffic_control_target_id is not None:
            result['TrafficControlTargetId'] = self.traffic_control_target_id

        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')

        if m.get('ItemConditionExpress') is not None:
            self.item_condition_express = m.get('ItemConditionExpress')

        if m.get('ItemConditionType') is not None:
            self.item_condition_type = m.get('ItemConditionType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewProductRegulation') is not None:
            self.new_product_regulation = m.get('NewProductRegulation')

        if m.get('RecallName') is not None:
            self.recall_name = m.get('RecallName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SplitParts') is not None:
            temp_model = main_models.GetTrafficControlTargetResponseBodySplitParts()
            self.split_parts = temp_model.from_map(m.get('SplitParts'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatisPeriod') is not None:
            self.statis_period = m.get('StatisPeriod')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ToleranceValue') is not None:
            self.tolerance_value = m.get('ToleranceValue')

        if m.get('TrafficControlTargetId') is not None:
            self.traffic_control_target_id = m.get('TrafficControlTargetId')

        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetTrafficControlTargetResponseBodySplitParts(DaraModel):
    def __init__(
        self,
        set_points: List[int] = None,
        set_values: List[int] = None,
        time_points: List[int] = None,
    ):
        self.set_points = set_points
        self.set_values = set_values
        self.time_points = time_points

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.set_points is not None:
            result['SetPoints'] = self.set_points

        if self.set_values is not None:
            result['SetValues'] = self.set_values

        if self.time_points is not None:
            result['TimePoints'] = self.time_points

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SetPoints') is not None:
            self.set_points = m.get('SetPoints')

        if m.get('SetValues') is not None:
            self.set_values = m.get('SetValues')

        if m.get('TimePoints') is not None:
            self.time_points = m.get('TimePoints')

        return self

