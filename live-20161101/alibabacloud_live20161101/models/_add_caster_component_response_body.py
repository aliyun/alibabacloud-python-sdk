# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCasterComponentResponseBody(DaraModel):
    def __init__(
        self,
        component_id: str = None,
        request_id: str = None,
    ):
        # The component ID. The value can be used as the value of a request parameter to query, modify, or delete a production studio.
        self.component_id = component_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

