# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCategoryRequest(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
    ):
        # The category ID. Only a single category ID is supported. You can obtain the category ID by using the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Asset Management Configuration** > **Category Management** to view the category ID.
        # - Obtain the category ID from the response of the [AddCategory](~~AddCategory~~) operation when you create a category.
        # 
        # > If the specified category ID is the ID of a parent category, the parent category and all its subcategories are deleted. Proceed with caution.
        # 
        # This parameter is required.
        self.cate_id = cate_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        return self

