# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLaboratoriesRequest(DaraModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        scene_id: str = None,
        status: str = None,
    ):
        # The laboratory environment.
        # 
        # - `Daily`: the daily environment
        # 
        # - `Pre`: the pre-production environment
        # 
        # - `Prod`: the production environment
        self.environment = environment
        # The ID of the instance. You can obtain this ID by calling the `ListInstances` API.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the scene. You can obtain this ID by calling the `ListScenes` API.
        # 
        # This parameter is required.
        self.scene_id = scene_id
        # The laboratory status.
        # 
        # - `Offline`: The laboratory is offline.
        # 
        # - `Online`: The laboratory is online.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['Environment'] = self.environment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

