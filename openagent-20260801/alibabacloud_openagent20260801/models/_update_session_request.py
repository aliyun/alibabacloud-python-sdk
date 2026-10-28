# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSessionRequest(DaraModel):
    def __init__(
        self,
        pinned: bool = None,
        title: str = None,
    ):
        # Specifies whether to pin the session. If you do not specify this parameter, the pinned status remains unchanged.
        self.pinned = pinned
        # The new title of the session. If you do not need to update the title, do not specify this parameter.
        self.title = title

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pinned') is not None:
            self.pinned = m.get('pinned')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

