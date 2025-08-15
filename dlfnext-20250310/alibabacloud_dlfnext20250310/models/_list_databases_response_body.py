# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDatabasesResponseBody(DaraModel):
    def __init__(
        self,
        databases: List[str] = None,
        next_page_token: str = None,
    ):
        self.databases = databases
        self.next_page_token = next_page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.databases is not None:
            result['databases'] = self.databases

        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databases') is not None:
            self.databases = m.get('databases')

        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')

        return self

