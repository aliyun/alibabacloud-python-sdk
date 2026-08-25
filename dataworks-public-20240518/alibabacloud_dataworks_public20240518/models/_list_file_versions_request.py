# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFileVersionsRequest(DaraModel):
    def __init__(
        self,
        file_id: int = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        project_identifier: str = None,
    ):
        # The ID of the file. You can call [ListFiles](https://help.aliyun.com/document_detail/173942.html) to query the file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The page number. Used for paging.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace. You can click the small wrench icon in the upper-right corner of the page to go to the storage management page and view the ID.
        self.project_id = project_id
        # The unique identifier of the DataWorks workspace, which is the English identifier displayed in the workspace switcher at the top of the DataStudio page.
        # 
        # You must set either this parameter or ProjectId to determine the DataWorks workspace for this API call.
        self.project_identifier = project_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        return self

