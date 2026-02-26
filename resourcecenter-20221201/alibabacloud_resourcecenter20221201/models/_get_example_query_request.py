# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetExampleQueryRequest(DaraModel):
    def __init__(
        self,
        query_id: str = None,
    ):
        # The ID of the template.
        # 
        # > You can call the [ListExampleQueries](~~ListExampleQueries~~) operation to obtain the template ID.
        # 
        # This parameter is required.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_id is not None:
            result['QueryId'] = self.query_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        return self

