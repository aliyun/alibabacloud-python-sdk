# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCasterLayoutResponseBody(DaraModel):
    def __init__(
        self,
        layout_id: str = None,
        request_id: str = None,
    ):
        # The ID of the layout. You can use this ID to query information about the layout.
        self.layout_id = layout_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

