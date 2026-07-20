# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListViewsResponseBody(DaraModel):
    def __init__(
        self,
        next_page_token: str = None,
        views: List[str] = None,
    ):
        self.next_page_token = next_page_token
        self.views = views

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_page_token is not None:
            result['nextPageToken'] = self.next_page_token

        if self.views is not None:
            result['views'] = self.views

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextPageToken') is not None:
            self.next_page_token = m.get('nextPageToken')

        if m.get('views') is not None:
            self.views = m.get('views')

        return self

