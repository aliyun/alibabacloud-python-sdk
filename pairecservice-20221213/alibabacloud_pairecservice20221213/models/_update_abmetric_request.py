# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateABMetricRequest(DaraModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        instance_id: str = None,
        left_metric_id: str = None,
        name: str = None,
        operator: str = None,
        realtime: bool = None,
        result_resource_id: str = None,
        right_metric_id: str = None,
        scene_id: str = None,
        statistics_cycle: int = None,
        table_meta_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.definition = definition
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        self.left_metric_id = left_metric_id
        # This parameter is required.
        self.name = name
        self.operator = operator
        # This parameter is required.
        self.realtime = realtime
        self.result_resource_id = result_resource_id
        self.right_metric_id = right_metric_id
        # This parameter is required.
        self.scene_id = scene_id
        self.statistics_cycle = statistics_cycle
        # This parameter is required.
        self.table_meta_id = table_meta_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definition is not None:
            result['Definition'] = self.definition

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.left_metric_id is not None:
            result['LeftMetricId'] = self.left_metric_id

        if self.name is not None:
            result['Name'] = self.name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.realtime is not None:
            result['Realtime'] = self.realtime

        if self.result_resource_id is not None:
            result['ResultResourceId'] = self.result_resource_id

        if self.right_metric_id is not None:
            result['RightMetricId'] = self.right_metric_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.statistics_cycle is not None:
            result['StatisticsCycle'] = self.statistics_cycle

        if self.table_meta_id is not None:
            result['TableMetaId'] = self.table_meta_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LeftMetricId') is not None:
            self.left_metric_id = m.get('LeftMetricId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')

        if m.get('ResultResourceId') is not None:
            self.result_resource_id = m.get('ResultResourceId')

        if m.get('RightMetricId') is not None:
            self.right_metric_id = m.get('RightMetricId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('StatisticsCycle') is not None:
            self.statistics_cycle = m.get('StatisticsCycle')

        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

