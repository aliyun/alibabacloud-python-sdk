# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetABMetricGroupResponseBody(DaraModel):
    def __init__(
        self,
        abmetric_ids: str = None,
        abmetric_names: str = None,
        description: str = None,
        name: str = None,
        owner: str = None,
        realtime: bool = None,
        request_id: str = None,
        scene_id: str = None,
    ):
        self.abmetric_ids = abmetric_ids
        self.abmetric_names = abmetric_names
        self.description = description
        self.name = name
        self.owner = owner
        self.realtime = realtime
        self.request_id = request_id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

