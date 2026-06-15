# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MassPushV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        idempotent_token: str = None,
        push_tasks_shrink: str = None,
    ):
        # AppKey value.
        # 
        # This parameter is required.
        self.app_key = app_key
        # An idempotency token to prevent duplicate pushes caused by API retries. If you call this API with the same IdempotentToken within 15 minutes, only one push is sent. Subsequent calls return the result of the first successful push.
        # 
        # > - The token must be a standard 36-character UUID in 8-4-4-4-12 format. Valid characters are hexadecimal digits 0–9 and a–f. Case does not matter.
        # >
        # > - This parameter prevents duplicates only from retries. It does not prevent duplicates from concurrent calls.
        self.idempotent_token = idempotent_token
        # Batch push tasks.
        # 
        # This parameter is required.
        self.push_tasks_shrink = push_tasks_shrink

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

        if self.push_tasks_shrink is not None:
            result['PushTasks'] = self.push_tasks_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('IdempotentToken') is not None:
            self.idempotent_token = m.get('IdempotentToken')

        if m.get('PushTasks') is not None:
            self.push_tasks_shrink = m.get('PushTasks')

        return self

