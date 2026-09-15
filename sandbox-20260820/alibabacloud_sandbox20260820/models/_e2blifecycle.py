# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class E2BLifecycle(DaraModel):
    def __init__(
        self,
        auto_resume: bool = None,
        on_timeout: str = None,
    ):
        self.auto_resume = auto_resume
        self.on_timeout = on_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_resume is not None:
            result['autoResume'] = self.auto_resume

        if self.on_timeout is not None:
            result['onTimeout'] = self.on_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoResume') is not None:
            self.auto_resume = m.get('autoResume')

        if m.get('onTimeout') is not None:
            self.on_timeout = m.get('onTimeout')

        return self

