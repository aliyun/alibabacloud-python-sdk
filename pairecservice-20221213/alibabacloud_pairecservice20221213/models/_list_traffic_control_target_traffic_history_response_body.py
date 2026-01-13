# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListTrafficControlTargetTrafficHistoryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: str = None,
        traffic_control_task_traffic_histories: List[main_models.ListTrafficControlTargetTrafficHistoryResponseBodyTrafficControlTaskTrafficHistories] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.traffic_control_task_traffic_histories = traffic_control_task_traffic_histories

    def validate(self):
        if self.traffic_control_task_traffic_histories:
            for v1 in self.traffic_control_task_traffic_histories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TrafficControlTaskTrafficHistories'] = []
        if self.traffic_control_task_traffic_histories is not None:
            for k1 in self.traffic_control_task_traffic_histories:
                result['TrafficControlTaskTrafficHistories'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.traffic_control_task_traffic_histories = []
        if m.get('TrafficControlTaskTrafficHistories') is not None:
            for k1 in m.get('TrafficControlTaskTrafficHistories'):
                temp_model = main_models.ListTrafficControlTargetTrafficHistoryResponseBodyTrafficControlTaskTrafficHistories()
                self.traffic_control_task_traffic_histories.append(temp_model.from_map(k1))

        return self

class ListTrafficControlTargetTrafficHistoryResponseBodyTrafficControlTaskTrafficHistories(DaraModel):
    def __init__(
        self,
        experiment_id: str = None,
        item_id: str = None,
        record_time: str = None,
        traffic_control_target_aim_traffic: float = None,
        traffic_control_target_traffic: float = None,
        traffic_control_task_traffic: float = None,
    ):
        self.experiment_id = experiment_id
        self.item_id = item_id
        self.record_time = record_time
        self.traffic_control_target_aim_traffic = traffic_control_target_aim_traffic
        self.traffic_control_target_traffic = traffic_control_target_traffic
        self.traffic_control_task_traffic = traffic_control_task_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.record_time is not None:
            result['RecordTime'] = self.record_time

        if self.traffic_control_target_aim_traffic is not None:
            result['TrafficControlTargetAimTraffic'] = self.traffic_control_target_aim_traffic

        if self.traffic_control_target_traffic is not None:
            result['TrafficControlTargetTraffic'] = self.traffic_control_target_traffic

        if self.traffic_control_task_traffic is not None:
            result['TrafficControlTaskTraffic'] = self.traffic_control_task_traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('RecordTime') is not None:
            self.record_time = m.get('RecordTime')

        if m.get('TrafficControlTargetAimTraffic') is not None:
            self.traffic_control_target_aim_traffic = m.get('TrafficControlTargetAimTraffic')

        if m.get('TrafficControlTargetTraffic') is not None:
            self.traffic_control_target_traffic = m.get('TrafficControlTargetTraffic')

        if m.get('TrafficControlTaskTraffic') is not None:
            self.traffic_control_task_traffic = m.get('TrafficControlTaskTraffic')

        return self

