# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LinkImageRequest(DaraModel):
    def __init__(
        self,
        camera_height: int = None,
        file_name: str = None,
        platform: str = None,
        sub_scene_id: str = None,
    ):
        self.camera_height = camera_height
        # This parameter is required.
        self.file_name = file_name
        self.platform = platform
        # This parameter is required.
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.camera_height is not None:
            result['CameraHeight'] = self.camera_height

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraHeight') is not None:
            self.camera_height = m.get('CameraHeight')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')

        return self

