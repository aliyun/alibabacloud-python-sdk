# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTextbookAssistantSceneDetailsRequest(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        scene_id_list: List[str] = None,
    ):
        self.auth_token = auth_token
        self.scene_id_list = scene_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        if self.scene_id_list is not None:
            result['sceneIdList'] = self.scene_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('sceneIdList') is not None:
            self.scene_id_list = m.get('sceneIdList')

        return self

