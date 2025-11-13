# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunLegalAdviceConsultationShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        assistant_shrink: str = None,
        extra_shrink: str = None,
        stream: bool = None,
        thread_shrink: str = None,
    ):
        self.app_id = app_id
        self.assistant_shrink = assistant_shrink
        self.extra_shrink = extra_shrink
        self.stream = stream
        self.thread_shrink = thread_shrink

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

        if self.extra_shrink is not None:
            result['extra'] = self.extra_shrink

        if self.stream is not None:
            result['stream'] = self.stream

        if self.thread_shrink is not None:
            result['thread'] = self.thread_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('assistant') is not None:
            self.assistant_shrink = m.get('assistant')

        if m.get('extra') is not None:
            self.extra_shrink = m.get('extra')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('thread') is not None:
            self.thread_shrink = m.get('thread')

        return self

