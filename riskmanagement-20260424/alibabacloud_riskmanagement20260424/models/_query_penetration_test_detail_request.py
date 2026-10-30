# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPenetrationTestDetailRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
    ):
        # The unique identity of the application record.
        # 
        # > This field is of the Long type. Precision loss may occur during the procedure to serialize or deserialize the numeric sequence. Ensure that the value does not exceed 9007199254740991.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

