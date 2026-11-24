# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSessionRequest(DaraModel):
    def __init__(
        self,
        title: str = None,
        ui_enabled: bool = None,
    ):
        # The session title.
        self.title = title
        # Specifies whether to enable session UI enhancement. Only common sessions support this feature.
        self.ui_enabled = ui_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['title'] = self.title

        if self.ui_enabled is not None:
            result['uiEnabled'] = self.ui_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('uiEnabled') is not None:
            self.ui_enabled = m.get('uiEnabled')

        return self

