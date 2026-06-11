# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPromptsRequest(DaraModel):
    def __init__(
        self,
        biz_tags: str = None,
        namespace_id: str = None,
        page_no: int = None,
        page_size: int = None,
        prompt_key: str = None,
        search: str = None,
    ):
        self.biz_tags = biz_tags
        # This parameter is required.
        self.namespace_id = namespace_id
        self.page_no = page_no
        self.page_size = page_size
        self.prompt_key = prompt_key
        self.search = search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tags is not None:
            result['BizTags'] = self.biz_tags

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.prompt_key is not None:
            result['PromptKey'] = self.prompt_key

        if self.search is not None:
            result['Search'] = self.search

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTags') is not None:
            self.biz_tags = m.get('BizTags')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PromptKey') is not None:
            self.prompt_key = m.get('PromptKey')

        if m.get('Search') is not None:
            self.search = m.get('Search')

        return self

