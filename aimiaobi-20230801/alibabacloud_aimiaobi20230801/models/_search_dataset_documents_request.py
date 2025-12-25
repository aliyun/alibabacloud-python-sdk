# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchDatasetDocumentsRequest(DaraModel):
    def __init__(
        self,
        dataset_id: int = None,
        dataset_name: str = None,
        extend_1: str = None,
        include_content: bool = None,
        page_size: str = None,
        query: str = None,
        workspace_id: str = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.extend_1 = extend_1
        self.include_content = include_content
        self.page_size = page_size
        # This parameter is required.
        self.query = query
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.extend_1 is not None:
            result['Extend1'] = self.extend_1

        if self.include_content is not None:
            result['IncludeContent'] = self.include_content

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Extend1') is not None:
            self.extend_1 = m.get('Extend1')

        if m.get('IncludeContent') is not None:
            self.include_content = m.get('IncludeContent')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

