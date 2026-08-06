# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserRolesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        user_principal: str = None,
    ):
        # The number of entries per page.
        self.max_results = max_results
        # The pagination token used to retrieve the next page of data. If the response does not provide this token, pass an empty string ("").
        self.page_token = page_token
        # The resource descriptor for the user.
        self.user_principal = user_principal

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

        if self.user_principal is not None:
            result['userPrincipal'] = self.user_principal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')

        if m.get('userPrincipal') is not None:
            self.user_principal = m.get('userPrincipal')

        return self

