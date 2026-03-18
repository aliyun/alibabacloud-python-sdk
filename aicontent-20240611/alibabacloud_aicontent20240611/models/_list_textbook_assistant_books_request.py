# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTextbookAssistantBooksRequest(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        book_id: str = None,
        grade: str = None,
        max_results: str = None,
        page: str = None,
        version: str = None,
        volume: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        self.book_id = book_id
        self.grade = grade
        self.max_results = max_results
        self.page = page
        self.version = version
        self.volume = volume

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

        if self.grade is not None:
            result['grade'] = self.grade

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.page is not None:
            result['page'] = self.page

        if self.version is not None:
            result['version'] = self.version

        if self.volume is not None:
            result['volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('bookId') is not None:
            self.book_id = m.get('bookId')

        if m.get('grade') is not None:
            self.grade = m.get('grade')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('volume') is not None:
            self.volume = m.get('volume')

        return self

