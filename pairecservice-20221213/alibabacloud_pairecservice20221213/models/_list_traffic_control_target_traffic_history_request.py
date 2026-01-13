# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTrafficControlTargetTrafficHistoryRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        environment: str = None,
        experiment_group_id: str = None,
        experiment_id: str = None,
        instance_id: str = None,
        item_id: str = None,
        start_time: str = None,
        threshold: str = None,
    ):
        self.end_time = end_time
        self.environment = environment
        self.experiment_group_id = experiment_group_id
        self.experiment_id = experiment_id
        self.instance_id = instance_id
        self.item_id = item_id
        self.start_time = start_time
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id

        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')

        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

