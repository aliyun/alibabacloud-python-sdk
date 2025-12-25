# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConnDataRequest(DaraModel):
    def __init__(
        self,
        conn_data: str = None,
        scene_id: str = None,
    ):
        # This parameter is required.
        self.conn_data = conn_data
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_data is not None:
            result['ConnData'] = self.conn_data

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnData') is not None:
            self.conn_data = m.get('ConnData')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

