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

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

