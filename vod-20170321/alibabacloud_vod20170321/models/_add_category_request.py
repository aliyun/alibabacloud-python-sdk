# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCategoryRequest(DaraModel):
    def __init__(
        self,
        cate_name: str = None,
        parent_id: int = None,
        type: str = None,
    ):
        # The category name.
        # - Maximum length: 64 bytes.
        # - UTF-8 encoded.
        # 
        # This parameter is required.
        self.cate_name = cate_name
        # The parent category ID.
        # 
        # Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Management Configuration** > **Category Management** > **Audio/Video/Image Categories** or **Short Video Material Categories** to view category IDs.
        # 
        # > - If you specify this parameter, a subcategory is created under the specified parent category. If you do not specify this parameter, a level-0 category is created.
        # > - Because all level-0 categories for short video materials are built-in and cannot be modified, added, or deleted, only subcategories can be created under level-0 categories. Therefore, this parameter is required when `Type` is set to `material`.
        self.parent_id = parent_id
        # The category type. Valid values:
        # 
        # - **default** (default): audio/video/image category.
        # - **material**: short video material category.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

