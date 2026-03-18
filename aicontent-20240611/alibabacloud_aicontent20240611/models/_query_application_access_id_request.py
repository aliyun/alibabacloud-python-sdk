# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryApplicationAccessIdRequest(DaraModel):
    def __init__(
        self,
        application_access_id: str = None,
    ):
        self.application_access_id = application_access_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')

        return self

