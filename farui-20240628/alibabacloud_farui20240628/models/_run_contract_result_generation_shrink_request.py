# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunContractResultGenerationShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        assistant_shrink: str = None,
        stream: bool = None,
    ):
        self.app_id = app_id
        self.assistant_shrink = assistant_shrink
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.assistant_shrink is not None:
            result['assistant'] = self.assistant_shrink

        if self.stream is not None:
            result['stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('assistant') is not None:
            self.assistant_shrink = m.get('assistant')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        return self

