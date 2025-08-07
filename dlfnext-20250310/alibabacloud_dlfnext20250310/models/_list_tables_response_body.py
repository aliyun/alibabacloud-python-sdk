# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from typing import List


class ListTablesResponseBody(DaraModel):
    def __init__(
        self,
        next_page_token: str = None,
        tables: List[str] = None,
    ):
        self.next_page_token = next_page_token
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token

        if self.tables is not None:
            result['tables'] = self.tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')

        if m.get('tables') is not None:
            self.tables = m.get('tables')

        return self

