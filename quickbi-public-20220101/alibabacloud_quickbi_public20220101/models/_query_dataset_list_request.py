# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDatasetListRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        with_children: bool = None,
        workspace_id: str = None,
    ):
        # The ID of the request.
        self.directory_id = directory_id
        # Information about the directory where the dataset is located
        self.keyword = keyword
        # The ID of the workspace.
        self.page_num = page_num
        # Specifies the directory ID.
        # 
        # *   If this field is not empty, all datasets in the directory are obtained.
        self.page_size = page_size
        # The total number of pages returned.
        self.with_children = with_children
        # The name of the data source.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.with_children is not None:
            result['WithChildren'] = self.with_children

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('WithChildren') is not None:
            self.with_children = m.get('WithChildren')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

