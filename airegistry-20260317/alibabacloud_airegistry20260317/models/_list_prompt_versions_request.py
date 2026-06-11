# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPromptVersionsRequest(DaraModel):
    def __init__(
        self,
        namespace_id: str = None,
        page_no: int = None,
        page_size: int = None,
        prompt_key: str = None,
    ):
        # This parameter is required.
        self.namespace_id = namespace_id
        self.page_no = page_no
        self.page_size = page_size
        # This parameter is required.
        self.prompt_key = prompt_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.prompt_key is not None:
            result['PromptKey'] = self.prompt_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PromptKey') is not None:
            self.prompt_key = m.get('PromptKey')

        return self

