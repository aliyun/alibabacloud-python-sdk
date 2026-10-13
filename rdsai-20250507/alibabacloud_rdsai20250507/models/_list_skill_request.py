# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSkillRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        scope: str = None,
        sort: str = None,
        source: str = None,
        workspace_id: str = None,
    ):
        # The supported languages. Valid values:
        # 
        # * zh-CN: Simplified Chinese
        # * zh-TW: Traditional Chinese
        # * en-US: English
        # * ja-JP: Japanese
        self.language = language
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The search parameter for skill name or description. This filter is not currently enabled in the ContextDB management console.
        self.query = query
        # The ContextDB query scope. Valid values: all (default), private, and system.
        self.scope = scope
        # The sort parameter for skills. This sorting is not currently enabled in the ContextDB management console.
        self.sort = sort
        # The filter parameter for skill source. This filter is not currently enabled in the ContextDB management console.
        self.source = source
        # The ContextDB workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.source is not None:
            result['Source'] = self.source

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

