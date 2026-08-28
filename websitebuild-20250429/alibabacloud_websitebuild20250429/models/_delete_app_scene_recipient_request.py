# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAppSceneRecipientRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        recipient_id: str = None,
        scene_id: str = None,
    ):
        # The business ID.
        self.biz_id = biz_id
        # The recipient ID.
        self.recipient_id = recipient_id
        # The scenario ID.
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

        if self.recipient_id is not None:
            result['RecipientId'] = self.recipient_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('RecipientId') is not None:
            self.recipient_id = m.get('RecipientId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

