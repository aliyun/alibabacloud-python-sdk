# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListFoldersForParentRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parent_folder_id: str = None,
        query_keyword: str = None,
        tag: List[main_models.ListFoldersForParentRequestTag] = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The ID of the parent folder.
        # 
        # If you leave this parameter empty, the information of the first-level subfolders of the Root folder is queried.
        self.parent_folder_id = parent_folder_id
        # The keyword used for the query, such as a folder name.
        # 
        # Fuzzy match is supported.
        self.query_keyword = query_keyword
        # The tags. This parameter specifies a filter condition.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id

        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')

        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListFoldersForParentRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListFoldersForParentRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

