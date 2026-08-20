# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSnapshotsRequest(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        limit: int = None,
        next_token: str = None,
        qualifier: str = None,
        session_id: str = None,
    ):
        # The function name.
        self.function_name = function_name
        # The maximum number of snapshots to return. Valid values: 1 to 100. Default value: 20.
        self.limit = limit
        # The pagination token used to retrieve more results.
        self.next_token = next_token
        # The function alias.
        self.qualifier = qualifier
        # The source session ID from which the snapshot was created. When specified, functionName must also be specified.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.limit is not None:
            result['limit'] = self.limit

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

