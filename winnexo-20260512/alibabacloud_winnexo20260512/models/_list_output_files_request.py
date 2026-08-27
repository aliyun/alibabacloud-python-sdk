# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOutputFilesRequest(DaraModel):
    def __init__(
        self,
        item_type: str = None,
        keyword: str = None,
        operating_object_name: str = None,
        page: int = None,
        page_size: int = None,
        shared_only: bool = None,
        tenant_id: str = None,
    ):
        # The type of the output item. Valid values: ppt, html, document, picture, slides, video, audio, email, and others.
        self.item_type = item_type
        # The keyword for searching. Matches output titles or item names.
        self.keyword = keyword
        # The name of the digital employee (operating object). Used to filter results by name.
        self.operating_object_name = operating_object_name
        # The page number, starting from 1.
        self.page = page
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size
        # Specifies whether to display only outputs and output items that have sharing enabled.
        self.shared_only = shared_only
        # The tenant ID. This is a common parameter. In winnexo-cli, pass it explicitly with --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.shared_only is not None:
            result['sharedOnly'] = self.shared_only

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sharedOnly') is not None:
            self.shared_only = m.get('sharedOnly')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

