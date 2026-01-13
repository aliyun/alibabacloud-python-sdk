# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListABMetricGroupsResponseBody(DaraModel):
    def __init__(
        self,
        abmetric_groups: List[main_models.ListABMetricGroupsResponseBodyABMetricGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.abmetric_groups = abmetric_groups
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.abmetric_groups:
            for v1 in self.abmetric_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ABMetricGroups'] = []
        if self.abmetric_groups is not None:
            for k1 in self.abmetric_groups:
                result['ABMetricGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abmetric_groups = []
        if m.get('ABMetricGroups') is not None:
            for k1 in m.get('ABMetricGroups'):
                temp_model = main_models.ListABMetricGroupsResponseBodyABMetricGroups()
                self.abmetric_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListABMetricGroupsResponseBodyABMetricGroups(DaraModel):
    def __init__(
        self,
        abmetric_group_id: str = None,
        abmetric_ids: str = None,
        abmetric_names: str = None,
        description: str = None,
        name: str = None,
        owner: str = None,
        realtime: bool = None,
        scene_id: str = None,
    ):
        self.abmetric_group_id = abmetric_group_id
        self.abmetric_ids = abmetric_ids
        self.abmetric_names = abmetric_names
        self.description = description
        self.name = name
        self.owner = owner
        self.realtime = realtime
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abmetric_group_id is not None:
            result['ABMetricGroupId'] = self.abmetric_group_id

        if self.abmetric_ids is not None:
            result['ABMetricIds'] = self.abmetric_ids

        if self.abmetric_names is not None:
            result['ABMetricNames'] = self.abmetric_names

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.realtime is not None:
            result['Realtime'] = self.realtime

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricGroupId') is not None:
            self.abmetric_group_id = m.get('ABMetricGroupId')

        if m.get('ABMetricIds') is not None:
            self.abmetric_ids = m.get('ABMetricIds')

        if m.get('ABMetricNames') is not None:
            self.abmetric_names = m.get('ABMetricNames')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

