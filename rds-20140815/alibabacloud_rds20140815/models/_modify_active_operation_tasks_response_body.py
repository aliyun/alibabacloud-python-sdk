# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyActiveOperationTasksResponseBody(DaraModel):
    def __init__(
        self,
        ids: str = None,
        request_id: str = None,
    ):
        # The ID of the O\\&M task. IDs are separated by commas (,).
        self.ids = ids
        # The ID of the region.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

