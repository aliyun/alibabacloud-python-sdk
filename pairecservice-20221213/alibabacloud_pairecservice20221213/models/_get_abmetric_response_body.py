# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetABMetricResponseBody(DaraModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        left_metric_id: str = None,
        name: str = None,
        operator: str = None,
        realtime: str = None,
        request_id: str = None,
        result_resource_id: str = None,
        result_table_meta_id: str = None,
        right_metric_id: str = None,
        scene_id: str = None,
        scene_name: str = None,
        statistics_cycle: int = None,
        table_meta_id: str = None,
        type: str = None,
    ):
        self.definition = definition
        self.description = description
        self.left_metric_id = left_metric_id
        self.name = name
        self.operator = operator
        self.realtime = realtime
        self.request_id = request_id
        self.result_resource_id = result_resource_id
        self.result_table_meta_id = result_table_meta_id
        self.right_metric_id = right_metric_id
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.statistics_cycle = statistics_cycle
        self.table_meta_id = table_meta_id
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

        if self.left_metric_id is not None:
            result['LeftMetricId'] = self.left_metric_id

        if self.name is not None:
            result['Name'] = self.name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.realtime is not None:
            result['Realtime'] = self.realtime

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_resource_id is not None:
            result['ResultResourceId'] = self.result_resource_id

        if self.result_table_meta_id is not None:
            result['ResultTableMetaId'] = self.result_table_meta_id

        if self.right_metric_id is not None:
            result['RightMetricId'] = self.right_metric_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

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

        if m.get('LeftMetricId') is not None:
            self.left_metric_id = m.get('LeftMetricId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultResourceId') is not None:
            self.result_resource_id = m.get('ResultResourceId')

        if m.get('ResultTableMetaId') is not None:
            self.result_table_meta_id = m.get('ResultTableMetaId')

        if m.get('RightMetricId') is not None:
            self.right_metric_id = m.get('RightMetricId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('StatisticsCycle') is not None:
            self.statistics_cycle = m.get('StatisticsCycle')

        if m.get('TableMetaId') is not None:
            self.table_meta_id = m.get('TableMetaId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

