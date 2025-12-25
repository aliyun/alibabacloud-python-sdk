# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListThreadsShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
        thread_id: str = None,
    ):
        self.filter_shrink = filter_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.status = status
        self.thread_id = thread_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_shrink is not None:
            result['filter'] = self.filter_shrink

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.status is not None:
            result['status'] = self.status

        if self.thread_id is not None:
            result['threadId'] = self.thread_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter_shrink = m.get('filter')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('threadId') is not None:
            self.thread_id = m.get('threadId')

        return self

