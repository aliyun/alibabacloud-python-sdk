# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSubSceneRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        scene_id: str = None,
        upload_type: str = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.scene_id = scene_id
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.upload_type is not None:
            result['UploadType'] = self.upload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')

        return self

