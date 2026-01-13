# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class GetTrafficControlTaskTrafficResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_task_traffic_info: main_models.GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfo = None,
    ):
        self.request_id = request_id
        self.traffic_control_task_traffic_info = traffic_control_task_traffic_info

    def validate(self):
        if self.traffic_control_task_traffic_info:
            self.traffic_control_task_traffic_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.traffic_control_task_traffic_info is not None:
            result['TrafficControlTaskTrafficInfo'] = self.traffic_control_task_traffic_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrafficControlTaskTrafficInfo') is not None:
            temp_model = main_models.GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfo()
            self.traffic_control_task_traffic_info = temp_model.from_map(m.get('TrafficControlTaskTrafficInfo'))

        return self

class GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfo(DaraModel):
    def __init__(
        self,
        target_traffics: List[main_models.GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfoTargetTraffics] = None,
        task_traffics: Dict[str, main_models.TrafficControlTaskTrafficInfoTaskTrafficsValue] = None,
    ):
        self.target_traffics = target_traffics
        self.task_traffics = task_traffics

    def validate(self):
        if self.target_traffics:
            for v1 in self.target_traffics:
                 if v1:
                    v1.validate()
        if self.task_traffics:
            for v1 in self.task_traffics.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TargetTraffics'] = []
        if self.target_traffics is not None:
            for k1 in self.target_traffics:
                result['TargetTraffics'].append(k1.to_map() if k1 else None)

        result['TaskTraffics'] = {}
        if self.task_traffics is not None:
            for k1, v1 in self.task_traffics.items():
                result['TaskTraffics'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target_traffics = []
        if m.get('TargetTraffics') is not None:
            for k1 in m.get('TargetTraffics'):
                temp_model = main_models.GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfoTargetTraffics()
                self.target_traffics.append(temp_model.from_map(k1))

        self.task_traffics = {}
        if m.get('TaskTraffics') is not None:
            for k1, v1 in m.get('TaskTraffics').items():
                temp_model = main_models.TrafficControlTaskTrafficInfoTaskTrafficsValue()
                self.task_traffics[k1] = temp_model.from_map(v1)

        return self

class GetTrafficControlTaskTrafficResponseBodyTrafficControlTaskTrafficInfoTargetTraffics(DaraModel):
    def __init__(
        self,
        data: Dict[str, main_models.TrafficControlTaskTrafficInfoTargetTrafficsDataValue] = None,
        traffic_control_target_id: str = None,
    ):
        self.data = data
        self.traffic_control_target_id = traffic_control_target_id

    def validate(self):
        if self.data:
            for v1 in self.data.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = {}
        if self.data is not None:
            for k1, v1 in self.data.items():
                result['Data'][k1] = v1.to_map() if v1 else None

        if self.traffic_control_target_id is not None:
            result['TrafficControlTargetId'] = self.traffic_control_target_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = {}
        if m.get('Data') is not None:
            for k1, v1 in m.get('Data').items():
                temp_model = main_models.TrafficControlTaskTrafficInfoTargetTrafficsDataValue()
                self.data[k1] = temp_model.from_map(v1)

        if m.get('TrafficControlTargetId') is not None:
            self.traffic_control_target_id = m.get('TrafficControlTargetId')

        return self

