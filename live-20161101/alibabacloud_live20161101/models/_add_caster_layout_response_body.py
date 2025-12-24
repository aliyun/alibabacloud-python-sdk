# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCasterLayoutResponseBody(DaraModel):
    def __init__(
        self,
        layout_id: str = None,
        request_id: str = None,
    ):
        # The ID of the layout.
        # 
        # Record the ID as it can be used to manage the layout being created.
        self.layout_id = layout_id
        # The ID of the request.
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

