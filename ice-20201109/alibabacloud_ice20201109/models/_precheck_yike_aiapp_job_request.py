# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrecheckYikeAIAppJobRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_params: str = None,
    ):
        self.app_id = app_id
        self.app_params = app_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_params is not None:
            result['AppParams'] = self.app_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppParams') is not None:
            self.app_params = m.get('AppParams')

        return self

