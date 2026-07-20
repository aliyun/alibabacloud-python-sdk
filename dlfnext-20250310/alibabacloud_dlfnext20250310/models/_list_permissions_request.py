# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPermissionsRequest(DaraModel):
    def __init__(
        self,
        database: str = None,
        function: str = None,
        max_results: int = None,
        page_token: str = None,
        principal: str = None,
        resource_type: str = None,
        table: str = None,
        view: str = None,
    ):
        self.database = database
        self.function = function
        self.max_results = max_results
        self.page_token = page_token
        self.principal = principal
        # This parameter is required.
        self.resource_type = resource_type
        self.table = table
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['database'] = self.database

        if self.function is not None:
            result['function'] = self.function

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.page_token is not None:
            result['pageToken'] = self.page_token

        if self.principal is not None:
            result['principal'] = self.principal

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.table is not None:
            result['table'] = self.table

        if self.view is not None:
            result['view'] = self.view

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('database') is not None:
            self.database = m.get('database')

        if m.get('function') is not None:
            self.function = m.get('function')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')

        if m.get('principal') is not None:
            self.principal = m.get('principal')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('table') is not None:
            self.table = m.get('table')

        if m.get('view') is not None:
            self.view = m.get('view')

        return self

