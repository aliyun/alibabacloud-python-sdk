# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiDatasourceRequest(DaraModel):
    def __init__(
        self,
        key_word: str = None,
        page_num: int = None,
        page_size: int = None,
        workspace_id: str = None,
    ):
        # The keyword of the API data source name.
        self.key_word = key_word
        # Current page number for API data source list:
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_num = page_num
        # The number of rows per page in a paged query.
        # 
        # *   Default value: 10.
        # *   Valid values: 1 to 100.
        self.page_size = page_size
        # The workspace ID.
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
        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

