# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateABMetricGroupRequest(DaraModel):
    def __init__(
        self,
        abmetric_ids: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        realtime: bool = None,
        scene_id: str = None,
    ):
        # The A/B metric IDs. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.abmetric_ids = abmetric_ids
        # The description of the metric group.
        # 
        # This parameter is required.
        self.description = description
        # The ID of the instance. You can call the [ListInstances](https://help.aliyun.com/document_detail/2411819.html) operation to obtain this ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the metric group.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether the metric group is a real-time metric group.
        # 
        # This parameter is required.
        self.realtime = realtime
        # The ID of the scene. You can call the [ListScenes](https://help.aliyun.com/document_detail/2402581.html) operation to obtain this ID.
        # 
        # This parameter is required.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.realtime is not None:
            result['Realtime'] = self.realtime

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ABMetricIds') is not None:
            self.abmetric_ids = m.get('ABMetricIds')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Realtime') is not None:
            self.realtime = m.get('Realtime')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

