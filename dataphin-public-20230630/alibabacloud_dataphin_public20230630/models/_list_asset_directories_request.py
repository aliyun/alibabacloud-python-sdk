# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListAssetDirectoriesRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListAssetDirectoriesRequestListQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The query parameters.
        # 
        # This parameter is required.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListAssetDirectoriesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListAssetDirectoriesRequestListQuery(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        max_level: int = None,
        page: int = None,
        page_size: int = None,
        parent_directory_id: int = None,
        topic_id: int = None,
    ):
        # The folder name keyword. Maximum length: 128 characters.
        self.keyword = keyword
        # The maximum number of expansion levels. This parameter takes effect only in browse mode. Valid values: 1 to 10.
        self.max_level = max_level
        # The page number. Default value: 1.
        self.page = page
        # The number of entries per page. Default value: 50. Valid values: 1 to 200.
        self.page_size = page_size
        # The parent folder ID. This parameter takes effect only in browse mode.
        self.parent_directory_id = parent_directory_id
        # The topic ID.
        # 
        # This parameter is required.
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_level is not None:
            result['MaxLevel'] = self.max_level

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_directory_id is not None:
            result['ParentDirectoryId'] = self.parent_directory_id

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxLevel') is not None:
            self.max_level = m.get('MaxLevel')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentDirectoryId') is not None:
            self.parent_directory_id = m.get('ParentDirectoryId')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        return self

