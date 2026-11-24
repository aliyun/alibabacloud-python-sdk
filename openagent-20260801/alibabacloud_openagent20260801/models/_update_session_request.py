# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSessionRequest(DaraModel):
    def __init__(
        self,
        pinned: bool = None,
        title: str = None,
        ui_enabled: bool = None,
    ):
        # Specifies whether to pin the session. If this parameter is not specified, the pinned status remains unchanged.
        self.pinned = pinned
        # The updated session title. You can leave this parameter empty if no update is required.
        self.title = title
        # Specifies whether to enable session UI enhancement. This feature is supported only for common sessions.
        self.ui_enabled = ui_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pinned is not None:
            result['pinned'] = self.pinned

        if self.title is not None:
            result['title'] = self.title

        if self.ui_enabled is not None:
            result['uiEnabled'] = self.ui_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pinned') is not None:
            self.pinned = m.get('pinned')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('uiEnabled') is not None:
            self.ui_enabled = m.get('uiEnabled')

        return self

