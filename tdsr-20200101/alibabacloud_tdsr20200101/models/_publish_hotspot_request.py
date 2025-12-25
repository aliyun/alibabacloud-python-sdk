# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishHotspotRequest(DaraModel):
    def __init__(
        self,
        param_tag: str = None,
        sub_scene_uuid: str = None,
    ):
        self.param_tag = param_tag
        self.sub_scene_uuid = sub_scene_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_tag is not None:
            result['ParamTag'] = self.param_tag

        if self.sub_scene_uuid is not None:
            result['SubSceneUuid'] = self.sub_scene_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamTag') is not None:
            self.param_tag = m.get('ParamTag')

        if m.get('SubSceneUuid') is not None:
            self.sub_scene_uuid = m.get('SubSceneUuid')

        return self

