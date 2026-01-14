# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAlipayUrlRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['app_id'] = self.app_id

        if self.workspace_id is not None:
            result['workspace_id'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')

        if m.get('workspace_id') is not None:
            self.workspace_id = m.get('workspace_id')

        return self

