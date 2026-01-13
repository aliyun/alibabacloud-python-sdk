# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class UpdateTrafficControlTaskTrafficRequest(DaraModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        traffics: List[main_models.UpdateTrafficControlTaskTrafficRequestTraffics] = None,
        new_param_3: str = None,
    ):
        self.environment = environment
        self.instance_id = instance_id
        self.traffics = traffics
        self.new_param_3 = new_param_3

    def validate(self):
        if self.traffics:
            for v1 in self.traffics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['Environment'] = self.environment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Traffics'] = []
        if self.traffics is not None:
            for k1 in self.traffics:
                result['Traffics'].append(k1.to_map() if k1 else None)

        if self.new_param_3 is not None:
            result['new-param-3'] = self.new_param_3

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.traffics = []
        if m.get('Traffics') is not None:
            for k1 in m.get('Traffics'):
                temp_model = main_models.UpdateTrafficControlTaskTrafficRequestTraffics()
                self.traffics.append(temp_model.from_map(k1))

        if m.get('new-param-3') is not None:
            self.new_param_3 = m.get('new-param-3')

        return self

class UpdateTrafficControlTaskTrafficRequestTraffics(DaraModel):
    def __init__(
        self,
        item_or_experiment_id: str = None,
        record_time: str = None,
        traffic_control_target_aim_traffic: float = None,
        traffic_control_target_id: str = None,
        traffic_control_target_traffic: int = None,
        traffic_control_task_traffic: int = None,
    ):
        self.item_or_experiment_id = item_or_experiment_id
        self.record_time = record_time
        self.traffic_control_target_aim_traffic = traffic_control_target_aim_traffic
        self.traffic_control_target_id = traffic_control_target_id
        self.traffic_control_target_traffic = traffic_control_target_traffic
        self.traffic_control_task_traffic = traffic_control_task_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_or_experiment_id is not None:
            result['ItemOrExperimentId'] = self.item_or_experiment_id

        if self.record_time is not None:
            result['RecordTime'] = self.record_time

        if self.traffic_control_target_aim_traffic is not None:
            result['TrafficControlTargetAimTraffic'] = self.traffic_control_target_aim_traffic

        if self.traffic_control_target_id is not None:
            result['TrafficControlTargetId'] = self.traffic_control_target_id

        if self.traffic_control_target_traffic is not None:
            result['TrafficControlTargetTraffic'] = self.traffic_control_target_traffic

        if self.traffic_control_task_traffic is not None:
            result['TrafficControlTaskTraffic'] = self.traffic_control_task_traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemOrExperimentId') is not None:
            self.item_or_experiment_id = m.get('ItemOrExperimentId')

        if m.get('RecordTime') is not None:
            self.record_time = m.get('RecordTime')

        if m.get('TrafficControlTargetAimTraffic') is not None:
            self.traffic_control_target_aim_traffic = m.get('TrafficControlTargetAimTraffic')

        if m.get('TrafficControlTargetId') is not None:
            self.traffic_control_target_id = m.get('TrafficControlTargetId')

        if m.get('TrafficControlTargetTraffic') is not None:
            self.traffic_control_target_traffic = m.get('TrafficControlTargetTraffic')

        if m.get('TrafficControlTaskTraffic') is not None:
            self.traffic_control_task_traffic = m.get('TrafficControlTaskTraffic')

        return self

