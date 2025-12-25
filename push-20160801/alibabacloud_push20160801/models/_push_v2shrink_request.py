# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        idempotent_token: str = None,
        push_task_shrink: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        self.idempotent_token = idempotent_token
        # This parameter is required.
        self.push_task_shrink = push_task_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.idempotent_token is not None:
            result['IdempotentToken'] = self.idempotent_token

        if self.push_task_shrink is not None:
            result['PushTask'] = self.push_task_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('IdempotentToken') is not None:
            self.idempotent_token = m.get('IdempotentToken')

        if m.get('PushTask') is not None:
            self.push_task_shrink = m.get('PushTask')

        return self

