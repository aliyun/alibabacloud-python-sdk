# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTextbookAssistantBookDirectoriesRequest(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        book_id: str = None,
        scenario: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.book_id = book_id
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        if self.book_id is not None:
            result['bookId'] = self.book_id

        if self.scenario is not None:
            result['scenario'] = self.scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('bookId') is not None:
            self.book_id = m.get('bookId')

        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')

        return self

