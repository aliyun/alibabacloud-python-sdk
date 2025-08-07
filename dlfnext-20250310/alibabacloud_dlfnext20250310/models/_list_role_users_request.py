# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class ListRoleUsersRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        page_token: str = None,
        role_principal: str = None,
    ):
        self.max_results = max_results
        self.page_token = page_token
        self.role_principal = role_principal

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

        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')

        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')

        return self

