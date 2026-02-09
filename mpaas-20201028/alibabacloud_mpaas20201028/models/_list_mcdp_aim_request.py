# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMcdpAimRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        empty_tag: str = None,
        keyword: str = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        sort: str = None,
        sort_field: str = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.empty_tag = empty_tag
        self.keyword = keyword
        self.name = name
        self.page_no = page_no
        self.page_size = page_size
        self.sort = sort
        self.sort_field = sort_field
        self.tenant_id = tenant_id
        self.type = type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.empty_tag is not None:
            result['EmptyTag'] = self.empty_tag

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.name is not None:
            result['Name'] = self.name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EmptyTag') is not None:
            self.empty_tag = m.get('EmptyTag')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

