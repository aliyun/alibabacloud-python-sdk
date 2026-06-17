# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NotifyAppNotificationForAdminRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        env: str = None,
        payload: str = None,
        scene_id: str = None,
    ):
        # The business ID.
        self.biz_id = biz_id
        # The environment identifier.
        self.env = env
        self.payload = payload
        # The scene ID.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.env is not None:
            result['Env'] = self.env

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

