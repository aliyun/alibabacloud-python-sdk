# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProvisionConfigsRequest(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The name of the function. If this parameter is not specified, the provisioned configurations of all functions are listed.
        self.function_name = function_name
        # Number of provisioned configurations to return.
        self.limit = limit
        # A pagination token.
        self.next_token = next_token

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

