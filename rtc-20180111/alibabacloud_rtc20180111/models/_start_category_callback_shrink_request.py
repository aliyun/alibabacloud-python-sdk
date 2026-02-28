# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartCategoryCallbackShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        callback_shrink: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.callback_shrink = callback_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.callback_shrink is not None:
            result['Callback'] = self.callback_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Callback') is not None:
            self.callback_shrink = m.get('Callback')

        return self

