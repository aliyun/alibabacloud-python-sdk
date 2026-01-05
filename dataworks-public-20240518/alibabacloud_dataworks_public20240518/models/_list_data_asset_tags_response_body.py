# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataAssetTagsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDataAssetTagsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDataAssetTagsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataAssetTagsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        data_asset_tags: List[main_models.ListDataAssetTagsResponseBodyPagingInfoDataAssetTags] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The tags.
        self.data_asset_tags = data_asset_tags
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data_asset_tags:
            for v1 in self.data_asset_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataAssetTags'] = []
        if self.data_asset_tags is not None:
            for k1 in self.data_asset_tags:
                result['DataAssetTags'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_asset_tags = []
        if m.get('DataAssetTags') is not None:
            for k1 in m.get('DataAssetTags'):
                temp_model = main_models.ListDataAssetTagsResponseBodyPagingInfoDataAssetTags()
                self.data_asset_tags.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataAssetTagsResponseBodyPagingInfoDataAssetTags(DaraModel):
    def __init__(
        self,
        category: str = None,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        key: str = None,
        managers: List[str] = None,
        modify_time: int = None,
        modify_user: str = None,
        value_type: str = None,
        values: List[str] = None,
    ):
        # The type of the tag.
        # 
        # Valid values:
        # 
        # *   Normal
        # *   System
        self.category = category
        # The time when the tag was created.
        self.create_time = create_time
        # The creator of the tag.
        self.create_user = create_user
        # The description of the tag.
        self.description = description
        # The tag key.
        self.key = key
        # The tag administrators.
        self.managers = managers
        # The time when the tag was last modified.
        self.modify_time = modify_time
        # The user who last modified the tag.
        self.modify_user = modify_user
        # The type of the tag value.
        self.value_type = value_type
        # The tag values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        if self.managers is not None:
            result['Managers'] = self.managers

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Managers') is not None:
            self.managers = m.get('Managers')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

