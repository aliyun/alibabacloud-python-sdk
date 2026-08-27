# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class ListKnowledgeBaseDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        directories: List[Any] = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The status code.
        self.code = code
        # The directory titles.
        self.directories = directories
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The total number of results.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.directories is not None:
            result['directories'] = self.directories

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('directories') is not None:
            self.directories = m.get('directories')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

