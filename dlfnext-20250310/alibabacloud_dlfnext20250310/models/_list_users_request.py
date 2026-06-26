# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUsersRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        type: str = None,
        user_name: str = None,
    ):
        # The number of entries to return on each page.
        self.max_results = max_results
        # The pagination token used to retrieve the next page of results. If this parameter is not returned in the response, pass an empty string ("").
        self.page_token = page_token
        # The type of the user.
        self.type = type
        # The user name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.page_token is not None:
            result['pageToken'] = self.page_token

        if self.type is not None:
            result['type'] = self.type

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

