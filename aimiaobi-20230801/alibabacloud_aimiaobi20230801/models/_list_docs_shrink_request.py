# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDocsShrinkRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        doc_name: str = None,
        doc_type: str = None,
        max_results: int = None,
        next_token: str = None,
        skip: int = None,
        statuses_shrink: str = None,
        workspace_id: str = None,
    ):
        self.category_id = category_id
        self.doc_name = doc_name
        self.doc_type = doc_type
        self.max_results = max_results
        self.next_token = next_token
        self.skip = skip
        self.statuses_shrink = statuses_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.statuses_shrink is not None:
            result['Statuses'] = self.statuses_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Statuses') is not None:
            self.statuses_shrink = m.get('Statuses')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

