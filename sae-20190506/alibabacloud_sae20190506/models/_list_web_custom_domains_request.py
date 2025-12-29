# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWebCustomDomainsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        limit: int = None,
        namespace_id: str = None,
        next_token: str = None,
        prefix: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The number of custom domain names returned.
        self.limit = limit
        # The namespace ID.
        self.namespace_id = namespace_id
        # The pagination token.
        self.next_token = next_token
        # The prefix of the custom domain name that you want to query.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        return self

