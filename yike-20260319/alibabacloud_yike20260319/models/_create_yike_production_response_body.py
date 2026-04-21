# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateYikeProductionResponseBody(DaraModel):
    def __init__(
        self,
        production_id: str = None,
        request_id: str = None,
    ):
        self.production_id = production_id
        # RequestId
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

