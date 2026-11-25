# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCategoryRequest(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
    ):
        # The category ID. You can specify only one category ID. You can obtain the category ID by using one of the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Asset Management Configuration** > **Category Management** > **Audio/Video and Image Categories** or **Short Video Material Categories** to view the category ID.
        # - The category ID is returned when you call the [AddCategory](~~AddCategory~~) operation to create a category.
        # 
        # This parameter is required.
        self.cate_id = cate_id
        # The category name.
        # 
        # - The name can be up to 64 bytes in length.
        # - The name must be encoded in UTF-8.
        # 
        # This parameter is required.
        self.cate_name = cate_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        return self

