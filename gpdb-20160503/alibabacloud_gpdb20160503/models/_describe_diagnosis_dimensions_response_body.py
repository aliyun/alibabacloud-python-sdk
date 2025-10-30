# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDiagnosisDimensionsResponseBody(DaraModel):
    def __init__(
        self,
        databases: List[str] = None,
        request_id: str = None,
        user_names: List[str] = None,
    ):
        # The names of the databases.
        self.databases = databases
        # The request ID.
        self.request_id = request_id
        # The names of the database accounts.
        self.user_names = user_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.databases is not None:
            result['Databases'] = self.databases

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_names is not None:
            result['UserNames'] = self.user_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Databases') is not None:
            self.databases = m.get('Databases')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserNames') is not None:
            self.user_names = m.get('UserNames')

        return self

