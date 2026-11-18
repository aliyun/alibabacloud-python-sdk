# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListChatMessageContentsRequest(DaraModel):
    def __init__(
        self,
        max_chars_per_attachment: int = None,
        page: int = None,
        page_size: int = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # The maximum length of the attachment content.
        self.max_chars_per_attachment = max_chars_per_attachment
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the data source.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The ID of the effective tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_chars_per_attachment is not None:
            result['maxCharsPerAttachment'] = self.max_chars_per_attachment

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxCharsPerAttachment') is not None:
            self.max_chars_per_attachment = m.get('maxCharsPerAttachment')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

