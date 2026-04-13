# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceConnectionStringResponseBody(DaraModel):
    def __init__(
        self,
        modified_connection_string: str = None,
        request_id: str = None,
    ):
        self.modified_connection_string = modified_connection_string
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modified_connection_string is not None:
            result['ModifiedConnectionString'] = self.modified_connection_string

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifiedConnectionString') is not None:
            self.modified_connection_string = m.get('ModifiedConnectionString')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

