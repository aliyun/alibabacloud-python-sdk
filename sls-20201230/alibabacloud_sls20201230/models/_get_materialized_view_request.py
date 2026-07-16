# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMaterializedViewRequest(DaraModel):
    def __init__(
        self,
        return_status: bool = None,
    ):
        self.return_status = return_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.return_status is not None:
            result['returnStatus'] = self.return_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnStatus') is not None:
            self.return_status = m.get('returnStatus')

        return self

