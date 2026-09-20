# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataServiceFoldersRequest(DaraModel):
    def __init__(
        self,
        folder_name_keyword: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        # The keyword of the folder name. Substring matching is supported.
        self.folder_name_keyword = folder_name_keyword
        # The ID of the business process to which the folder belongs.
        self.group_id = group_id
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The tenant ID. To obtain the tenant ID, log on to the [DataWorks console](https://workbench.data.aliyun.com/console), go to the DataStudio page, click your username in the upper-right corner, and select Menu > User Info.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_name_keyword is not None:
            result['FolderNameKeyword'] = self.folder_name_keyword

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderNameKeyword') is not None:
            self.folder_name_keyword = m.get('FolderNameKeyword')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

