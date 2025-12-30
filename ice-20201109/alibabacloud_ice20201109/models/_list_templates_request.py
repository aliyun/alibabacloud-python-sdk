# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTemplatesRequest(DaraModel):
    def __init__(
        self,
        create_source: str = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        sort_type: str = None,
        status: str = None,
        type: str = None,
    ):
        # The source from which the template was created.
        # 
        # Valid values:
        # 
        # *   AliyunConsole
        # *   WebSDK
        # *   OpenAPI
        self.create_source = create_source
        # The search keyword. You can use the template ID or title as the keyword to search for templates.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 20. Valid values: 1 to 100.
        self.page_size = page_size
        # The sorting parameter. By default, the query results are sorted by creation time in descending order.
        # 
        # Valid values:
        # 
        # *   CreationTime:Asc: sorted by creation time in ascending order.
        # *   CreationTime:Desc: sorted by creation time in descending order.
        self.sort_type = sort_type
        # The template state.
        # 
        # Valid values:
        # 
        # *   UploadFailed: Failed to upload the video.
        # *   ProcessFailed: Failed to process the advanced template.
        # *   Available: The template is available.
        # *   Uploading: The video is being uploaded.
        # *   Created: The template is created but not ready for use.
        # *   Processing: The advanced template is being processed.
        self.status = status
        # The template type.
        # 
        # Valid values:
        # 
        # *   Timeline
        # *   VETemplate
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_source is not None:
            result['CreateSource'] = self.create_source

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

