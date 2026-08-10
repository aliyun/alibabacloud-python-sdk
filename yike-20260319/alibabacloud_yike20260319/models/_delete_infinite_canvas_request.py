# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInfiniteCanvasRequest(DaraModel):
    def __init__(
        self,
        canvas_id: str = None,
    ):
        # The ID of the infinite canvas.
        # 
        # This parameter is required.
        self.canvas_id = canvas_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.canvas_id is not None:
            result['CanvasId'] = self.canvas_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanvasId') is not None:
            self.canvas_id = m.get('CanvasId')

        return self

